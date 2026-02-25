---
category: til
created: 2023-10-02 16:39:00
tags:
- software
- design
title: Horizontal and vertical complexity in software
---

This is more of an opinion piece from the short blog [1], but it nicely summarizes what I've intuited about good and bad abstractions I've made. 

Writing short functions is good in general. When programmers first learn about it, they often split functions into smaller and smaller units. This usually ends badly (unless you're a top-tier programmer [^1] ), but I hadn't been able to vocalize why. The reason is that endlessly breaking apart functions can minimize *horizontal complexity* (where a top level script is smaller) but increase *vertical complexity* (where you have an extremely tall call stack).

When you successfully encapsulate some functionality, you've increased vertical complexity but in clean way. This is good. What does "successfully" mean?
- There are no "leaks" of your abstraction
- There are no bugs in implementation
- You have made a nice API which is intuitive to use, and you find it easy to call your own functions
- You don't forget and re-implement similar functions in other parts of the code
When any of these are not true, your encapsulation leads to more difficult debugging down the line. Something doesn't work in new code you're written: is it your new code's fault? Or is it one of the layers your pushed underneath?

This balance of horizontal vs. vertical complexity applies to all code we write. But in [1], the author is quoting some complexity swept under the rug for "educational purposes". When you'r teaching very new programmers, you often do have the urge to make things seem simple and easy so they don't get encouraged and quit. But the tradeoff is to not force them to learn your custom "educational API" or "educational library" to do pretty basic things. He gave an example where a class teaching beginning c programming used a custom input/output library which included things like `int get_int(void);` so that the class didn't need to learn what pointers were for the purposes of using `scanf`. 

This part of the articles made me freeze in my tracks: in my introduction to programming class in 2011, the professor wrote a custom c++ input/output library so that we didn't use `cin` or `cout`. As a result, when my software engineer friend mentioned `cout` the next semester and I had no idea what he was talking about, he said "wait, didn't you already take Intro to c++? How do you not know what `cout` is??" Even with 3 months of programming experience, I knew something was off, and I was annoyed enough with the class and professor that I felt programing was not for me (hilarious in hindsight). 
I couldn't remember exactly what library/API the professor, had us use, but the class website was still online [2], and lo and behold:

> Get input from the terminal (user)
`int getInt();  // Get an integer value from the terminal`

This was so surprising that I had to look up whether the professor took the class from this blogger, but I could not find online breadcrumbs enough to tell.


[^1]: I still remember the first time I saw [Peter Norvig's Jupyter notebook for the Advent of Code](https://github.com/norvig/pytudes/blob/main/ipynb/Advent-2018.ipynb). He did many things which weren't exactly Pythonic, but he had built up almost a domain specific language of functions and one-liners like `def nth(iterable, n): return next(islice(iter(iterable), n, n+1))` so that many solutions practically rolled off the tongue once you imagined the logic.
## References

1. https://blog.plover.com/prog/vertical-complexity.html
2. https://www.cs.tufts.edu/~sguyer/classes/comp11-2011s/ioreference.html

