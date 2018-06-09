---
title: 'MATLAB vs Python binary storage of matrices'
layout: post
categories: articles
---

A recent confusion for me was when I had to translate some MATLAB scripts that read from and wrote to binary files.
The files were just 16-bit integers from digital elevation maps (DEMs) that were supposed to be arranged into a matrix.

It seemed like I should have just been able to find the corresponding commands and things should work?
Turns out I finally had to learn what [**row-major** and **column-major order**](https://en.wikipedia.org/wiki/Row-_and_column-major_order) were after ignoring it many other times.

The reason? 
MATLAB decided to follow the footsteps of Fortran and use column-major order to save matrices, while Python followed C and every other C-like language and uses row-major.

The simplest way that made me get what I had to change was the following binary file test:

```bash
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
```

Note that `hexdump` is a unix command to display the contents of a file as a bunch of binary numbers.
You can use this on text files and it won't be very recognizable, but for matrices saved as binary files, you will see the numbers that were the matrix elements (the first column of `hexdump` is the position of the file.)

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


To match exactly the above picture exactly:

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
Note that to get back to a matrix from a file, we'll need to `reshape`:
```bash
>>> print(np.fromfile('test_py.bin', dtype='i2'))
[1 2 3 4 5 6 7 8 9]
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
