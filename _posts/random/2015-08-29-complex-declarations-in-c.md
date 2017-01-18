---
title: 'Complex Declarations in C'
layout: post
categories: random
redirect_from:
- /random/2015/08/29/complex/declarations/in/c
- /blog/2015/08/29/complex/declarations/in/c
---
# Reading Complex Variable Declarations in C

The way variables can be declared can get mind-bendingly difficult in C. While it is generally bad practice to make something so complex that a person has to spend a minute just figuring out what your variable does, it could be helpful to get the full rule set. 

There are a couple notes to keep in mind:

1. The bracket and parentheses (`[]` and `()`) operators, which appears to the right of a variable, take place over the `*` operator.
2. Brackets and parentheses have the same precedence from left to right.
3. You can use parentheses to override the default association order.

Some examples:

```C
int *ptrs_to_ints[5]  /* An array of 5 points to ints */

int (*ptr_to_array)[5]  /* A pointer to an array containing 5 ints */

int *(*pts_to_ptrs)[5]  /* A pointer to an array of 5 pointers to ints */
```


A helpful algorithm to follow [comes from here]():

1. Start with the identifier and look directly to the right for brackets or parentheses (if any).
2. Interpret these brackets or parentheses, then look to the left for asterisks.
3. If you encounter a right parenthesis at any stage, go back and apply rules 1 and 2 to everything within the parentheses.
4. Apply the type specifier.

However, strictly thinking in terms of these steps is probably only really necessary when you come across something like this:

```C
char *( *(*var)(int) )[10];
```
This can be read as "var is a pointer to a function taking in an int and returning a pointer to an an array of 10 pointers to chars".

Most more commonly seen declarators will be easier to understand.

For another algorithm of interpreting the most complex declarator, [see the spiral of death](http://c-faq.com/decl/spiral.anderson.html).
