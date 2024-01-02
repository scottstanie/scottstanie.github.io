---
title: 'MATLAB vs Python binary storage of matrices'
layout: default
categories: articles
---

I recently ran into some confusion when I had to translate some MATLAB scripts that read from and wrote to binary files.
The files were just 16-bit integers from digital elevation maps (DEMs) that were supposed to be arranged into a matrix.

Ideally I would have just found the equivalent commands and things would have worked.
Turns out I had to learn finally what [**row-major** and **column-major order**](https://en.wikipedia.org/wiki/Row-_and_column-major_order) meant.

MATLAB, being a descendant of Fortran, decided to follow its footsteps and use column-major order internally to store matrices. 
Python followed C and other C-like language, so it uses row-major.
This means they do not play nicely together without extra care.

The simplest test that made me understand what I had to change was the following:

{% highlight python linenos %}
def f(x):
    return 3 * x
{% endhighlight %}


{% highlight bash %}
$ python
>>> import numpy as np
>>> A = np.array([[1, 2],[3, 4]]).astype('int16')
>>> print(A)
[[1 2]
 [3 4]]
>>> A.tofile('test_py.bin')
>>> quit()

$ hexdump test_py.bin
0000000 0001 0002 0003 0004                    
0000008
{% endhighlight %}


Note that `hexdump` is a unix command to display the contents of a file as a bunch of binary numbers.
You can use this on text files and it won't be very recognizable, but for matrices saved as binary, you will see the numbers that were the matrix elements (the first column of `hexdump` is the position of the file.)

Everything looks normal for python.
However, things are different for MATLAB:

```bash
$ matlab -nodesktop -nodisplay
>> A = [1 2; 3 4]
A =
     1     2
     3     4
>> fwrite(fopen('test_matlab.bin', 'w'), A, 'uint16');
>> quit
$ hexdump test_matlab.bin
0000000 0001 0003 0002 0004                    
0000008
```


The other part I didn't understand before was that how a language stores a matrix **doesn't matter until you are saving it**.
Both these will work for normal matrix math and you don't need to think about it.
It's only when you are trying to match a specific binary format that the order matters, since the langauge will save the bytes in whichever order it uses.

{% include image.html url="/images/Row_and_column_major_order.svg" height="l40" width="340" description="Credit Wikipedia" %}


To demonstrate the above 3x3 picture:

```bash
$ python
>>> import numpy as np
>>> np.array([[1, 2, 3],[4,5,6],[7,8,9]]).astype('int16').tofile('test_py.bin')
>>> 
$ hexdump test_py.bin
0000000 0001 0002 0003 0004 0005 0006 0007 0008
0000010 0009                                   
0000012
```

```bash
$ matlab -nodesktop -nodisplay
>> A = [1 2 3; 4 5 6; 7 8 9];
>> fwrite(fopen('test_matlab.bin', 'w'), A, 'uint16');
>> quit
scott:scottstanie.github.io$ hexdump test_matlab.bin
0000000 0001 0004 0007 0002 0005 0008 0003 0006
0000010 0009                                   
0000012
```


#### Fixes for MATLAB

If we're working in MATLAB, this means we have to make two fixes if we are working with row-major saved data.
If we wanted MATLAB to match the Python/C order, we would need to just transpose the matrix before saving if we want python to read it correctly.

```bash
>> fwrite(fopen('test_for_python.bin', 'w'), A', 'uint16');
```

Second, we also need to change how we **read in** the binary data.
If we naively try to read in the matrix that numpy saved, it will be transposed due to MATLAB using column order:
```bash
>> A = fread(fopen('test_py.bin', 'rb'), [3 3], 'uint16')
A =
     1     4     7
     2     5     8
     3     6     9
```
So instead we need to transpose immediately after reading in the data:
```
>> A = fread(fopen('test_py.bin', 'rb'), [3 3], 'uint16')'
A =
     1     2     3
     4     5     6
     7     8     9
```

#### Fixes for Python

Now if we are working in Python and only reading to other users of Python/C, we don't need to worry about extra options, we can just use `np.tofile` and `np.fromfile`.
```bash
>>> print(np.fromfile('test_py.bin', dtype='i2'))
[1 2 3 4 5 6 7 8 9]
```

Note that to get back to a matrix from a file, we'll need to `reshape`:
```bash
>>> print(np.fromfile('test_py.bin', dtype='i2').reshape((3,3)))
[[1 2 3]
 [4 5 6]
 [7 8 9]]
```

If we happen to get a MATLAB user who's given us a file using the wrong (column-major) ordering:

```bash
>>> print(np.fromfile('test_matlab.bin', dtype='i2'))
[1 4 7 2 5 8 3 6 9]
>>> print(np.fromfile('test_matlab.bin', dtype='i2').reshape((3, 3)))
[[1 4 7]
 [2 5 8]
 [3 6 9]]
```

We can use numpy's built in option to handle Fortran/MATLAB using the `order='F'` argument to `reshape.
(We could also fix it by adding a `.T` at the end to transpose):

```bash
>>> print(np.fromfile('test_matlab.bin', dtype='i2').reshape((3, 3), order='F'))
[[1 2 3]
[4 5 6]
[7 8 9]]
```

The specific application this came up in was handling data from the [Shuttle Radar Topography Mission (SRTM)](https://www2.jpl.nasa.gov/srtm/faq.html) digital elevation maps.
They store all elevations for a square grid in row major order, using 16-bit **big-endian** format.

### Fixing byte order

Fuller explanations can be found online, but Wikipedia has a fine [short illustration](https://en.wikipedia.org/wiki/Endianness#Illustration).

Since everything on a computer is essentially stored in one long array one byte at a time, you have to pick which part of larger numbers (say, 16 bit integers) get stored first.

If you have the byte order wrong, the number 1 turns into 256, 2 turns into 512, and generally things become a mess.

#### How to handle byte order

An important thing to remember is that [the byte order of the machine shouldn't matter](https://commandcenter.blogspot.com/2012/04/byte-order-fallacy.html), only the order of the data you're working with.
Here', NASA tells us they use big-endian, so whichever machine we're using, we just need to tell the code that we're about to get some big-endian data.

How do we do this? It's relatively easy in both MATLAB and Python.
Let's say that `N20W100.hgt` is one of the DEM height files from the SRTM.
It's 16-bit integers, stored in big endian.

```bash
A = np.fromfile('N20W100.hgt', dtype='>i2').reshape((3601, 3601))
A = A.astype('<i2')
```

The `dtype='>i2'` the way to let numpy know we are getting a **big**-endian (hence greater than, >) 2 byte interger aka 16-bit integer.
The second line is if we want to put it into the more typical format of little endian, which most computers use nowadays.
You can also use numpy's `.byteswap()` function to switch big to little.

In MATLAB:
```bash
fid = fopen('N20W100.hgt','r','ieee-be');
A = fread(fid,[3601 3601],'int16');
A = A'
```
Pretty similar, with the caveat that we must transpose it for MATLAB.



