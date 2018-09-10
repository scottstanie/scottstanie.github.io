---
title: 'MATLAB vs Python Indexing for 3D data'
layout: post
categories: articles
---

I thought I had learned well enough what row-major and column-major order were [from my last confusion]({% post_url 2018-05-20-python-matlab-binary %}), but I didn't follow what the implications would be when moving from 2 indices to 3.

After learning image processing on MATLAB, I assumed that since a single image is indexed by `(row, column)`, `(row, column, image number)` was the most sensible order when dealing with multiple images
I had been confused by the first few Python tutorials I saw (like [this one for Tensorflow](https://www.tensorflow.org/tutorials/keras/basic_classification)), where for stacks of images, they use the *first* index for the image number rather than the *last*.

At first I assumed it was just some convention that different communities picked and stuck with.
The insight came when [I saw the following alternate explanation in the `numpy.reshape` docs](https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html):

> 'C' means to read / write the elements using C-like index order, with the last axis index changing fastest, back to the first axis index changing slowest. 
> 'F' means to read / write the elements using Fortran-like index order, with the first index changing fastest, and the last index changing slowest

With this version of row-major vs column-major, picking the first index for images seems completely natural.

## Illustration

Lets say we have two images, both are 3 x 4.
On the left we'll show image 1, and on the right image 2.
We'll show what the indexing looks like when you
Using the function `numpy.unravel_index` in Python, you can find what the 3-indexes are as you step through the linear indexes 0-23.

When we use this along with a `FuncAnimation`, we get a nice visual of the order pixels appear in the 3D stack:

{% include image.html url="/images/python_order.gif" description="Python row-order indexing for 2 images" height="380" width="520" %}

If we watch the title, we can see how indeed the last index changes quickest, and first index changes slowest.


The `unravel_index` function also takes an `order` keyword that allows you to specify 'F' for Fortran column-order (instead of the default 'C' for C/Python row-ordering).
Using this, we can also visualize what the linear order of pixels is in MATLAB/Fortran:

{% include image.html url="/images/matlab_order.gif" description="MATLAB's column-order indexing" height="380" width="520" %}

The two clear differences are 

1. Within a single image, the columns are what gets iterated over (hence 'column-major')
2. The title shows how the last index changes slowest, making it the natural candidate for representing image number.
