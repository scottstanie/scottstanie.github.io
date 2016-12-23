---
title: 'Iterators and Generators'
layout: default
categories: Random
---

# Iterables vs Iterators vs Generators

To summarize first:

- An ***iterable*** is a container-like object that can be iterated over.
  - Technically, it's a object that has an `__iter__()` method (equivalently, you can call `iter(x)` on this iterable)
  - For example, if `x = [1, 2, 3]`, x is the *iterable*, and calling `y = iter(x)` makes y the *iterator*
- A ***iterator*** is a lazy value producing factory
  - It is a object that has a `__next__()` method for producing the next value available
  - It will sit there and wait for something to call that method in order to `yield` that next value
- A ***generator*** is a specific type of iterator in python with elegant syntax.
  - A generator is an iterator, but not the other way around
  - The two types of generators are:
    - generator *functions*: any function with `yield`
    - generator *expressions*: like a list comprehension, but with parentheses
- Generators can be used to write better streaming code with fewer intermediate variables, less memory, and more efficient CPU usage
