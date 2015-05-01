---
title: 'Cartesian Products'
layout: default
---

# Cartesian products in python

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
