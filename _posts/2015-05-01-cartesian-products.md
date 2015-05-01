---
title: 'Cartesian Products'
layout: default
---

# Cartesian products in python

For intro to generators, [see here]({% post_url 2015-04-30-iterator-generator %})

#### What is a cartesian product? 

Mathematically, the cartesian product is an operator that acts on multiple sets and returns one set of all possible tuples from the sets. In set notation, the cartesian product of \\(A \times B \\) is:
$$
  A \times B = 
$$


#### A final note

For actual implementation of the cartesian product, you can just do:

    import itertools

    prods = itertools.product(choices, repeat=n)

    for p in prods:
        print p


This will print all products, yielding them one at a time

    (1, 1, 1)
    (1, 1, 2)
    (1, 1, 3)
    (1, 2, 1)
    (1, 2, 2)
    ...

ty python.  
![](http://imgs.xkcd.com/comics/python.png)
