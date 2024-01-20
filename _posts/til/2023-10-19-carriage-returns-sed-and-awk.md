---
created: 2023-10-19 16:36:00
tags:
- software
- tools
title: Carriage returns, `sed`, and `awk`
---

I had a large CSV that I wanted to analyze with `duckdb`. I was having a weird problem: I couldn't read it with`read_csv(...)` due to a confusing error:
```
Error: Invalid Input Error: Wrong NewLine Identifier. Expecting \r\n
```
I say "confusing" because I had specified `new_line='\n'`, so I don't know why it was expecting `\r\n`. But I assumed it was something with the line endings.

Oddly, if I split it up with my [`split.py`](https://gist.github.com/scottstanie/96ec6ecc8135a6675778b8add36e90ae), then used `read_csv('part_*csv', ...)` it would work fine.
But if I split it by year using [[Permanent/4 things to know about awk|awk]] :
```bash
for yy in `seq 2014 2023`; do
    awk -F';' -v "year=^$yy" '$2~year' all_bursts.csv > bursts_$yy.csv & 
done
```
then it still failed with the same problem.

I finally managed to open one of the smaller files and saw `^M` at the end, confirming that it [was from a newline problem](https://stackoverflow.com/questions/1110678/m-at-the-end-of-every-line-in-vim). The quickest way to fix it wasn't obvious, but in the end, `sed` was the simplest:

```bash
 sed -e 's/\r//' -i.bak all_bursts.csv
```
(which left me the `.bak` file in case I did it wrong)

But still, why was the python-split version working? 

To check, I made dummy file with some `\n` and some `\r\n` 
```python
f = open("test1", 'w')
f.write("aaa\nbbb\r\nccc\n")
```

If I simply `cat` the results, you can't tell...
```
$ cat test1
aaa
bbb
ccc
```
But there's a `-e` which `displays non-printing characters`, so the line endings get shown:
```bash
$ cat -e test1
aaa$
bbb^M$
ccc$
```

So this is what was messing up `duckdb`. How did python get rid of it? 
Apparently, `python` will automatically get rid of the double line ending when you `.write` to a file:
```python
>>> f = open("test1")
>>> f2 = open("test2", "w")
>>> for line in f:
...     f2.write(line)
...
4
4
4
```
Note the `4`! Even though 
```python
>>> f.write("aaa\nbbb\r\nccc\n")
13
```
gave 13 bytes written, the line-by-line writing only did `12` total, and the extra byte is gone:
```bash
$ cat -e test[12]
aaa$
bbb^M$
ccc$
aaa$
bbb$
ccc$
```

### What does the `\r` do in python?
I realized I didn't actually know what the "carriage return" did. It turns out the simple answer is "return to the line beginning".
So if we print one before a new line is printed, it will overwrite the existing text in the line:
```python
>>> print("This will be\roverwritten")
overwrittene
```


