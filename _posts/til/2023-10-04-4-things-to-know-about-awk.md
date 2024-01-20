---
created: 2023-10-04 16:41:00
tags:
- software
- tools
- bash
title: 4 Things to know about awk
---

1. **Language structure**: The basic format of scripts are
```awk
pattern1 { ACTION; ACTION; ... }

pattern2 { ACTION; ...}
```
The input is always one line at a time of a text file. Each pattern is checked; if it matches/passes, the actions within the braces are run. Also if you leave off the pattern, it runs the actions on every line, 

2. **Fields**: awk splits the files into "fields". You use `$1` to get the first column, `$2` for second, etc. `$0` prints the entire line. So if you want to rearrange the columns to be (4, 2, 3, 1), you'd write
```awk
{print $4, $2, $3, $1}
```

3. **Variables** You can initialize variables inside the brace of a `BEGIN { ... }` block:
```awk
# initialize a variable x to 0
BEGIN { x = 0 } 
# add up all of the second column
{ x += $2 }
# print it after going through all the lines
END { print x }
```
There are "special" variables, which include the input/output "field separator" `FS/OFS` (by default any amount of white space) or input/output "record separator" `RS/ORS` (by default `\n`)

4. **Comparisons**: You can do comparisons which are "fuzzy matching" like in javascript: numbers are coerced to strings, strings to numbers:
```awk
# print lines where column 1 is the string "a", column 2 is a number > 10
($1 == "a") && ($2 > 10) {print $0}
```

Based on (1), I just learned that why my most commonly used awk one liner, `ps aux | grep <blah> | awk {print $2} | xargs kill` will run on every line and has to be surrounded by braces.
	- Any apparently is redundant with the `grep`?  Now I know I can do `ps aux | awk '/blah/' {print $2}`


### References
1. https://ferd.ca/awk-in-20-minutes.html
2. https://learnxinyminutes.com/docs/awk/
