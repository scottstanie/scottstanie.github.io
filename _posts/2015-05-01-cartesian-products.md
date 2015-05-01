---
title: 'Cartesian Products'
layout: default
---

# Cartesian products in python

#### What is a cartesian product? 

Mathematically, the **cartesian product** is an operator that acts on multiple sets and returns one set of all possible tuples from the sets. In set notation, the cartesian product of \\(A \times B \\) is:
$$
  A \times B = \\{(a, b) \mid a \in A, b \in B\\}
$$

This can be extended beyond two sets- the legnth of the tuple is equal to the number of sets you are giving as input.

Now if we have a list of possible symbols, and we want every possible arrangement of them \\(n\\) times, we would use the **cartesian power**:
$$
  X\^n = \\{(x\_1, ... , x\_n) \mid x\_i \in X \quad \forall i \colon 1, ..., n \\}
$$

We are just repeating the same set \\(X\\) for each position in the n-tuple.

#### In python

So how can we product this in python? It is clear that for even moderate size inputs, if we were to keep every element of the product in memory, it would grow to a monstrous size. This is because with m symbols in X, for a n-tuple, we have a set of size \\(n\^m\\)  
This where where **generators** in python come in. For an intro to generators, [see here]({% post_url 2015-04-30-iterator-generator %})  
Our generator needs to `yield` each n-tuple one at a time as our function returns it.

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
