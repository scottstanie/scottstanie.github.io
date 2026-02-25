---
category: til
created: 2023-11-17 16:37:00
tags:
- software
- typing
- python
- mypy
title: Unions vs TypeVars with constraints
---


I have been heavily using the following type annotation in many functions which would "do stuff with a file", loosely:
```python
import os
from typing import Union, TypeAlias

Filename: TypeAlias = Union[str, os.PathLike[str]]
```
The main goal I had in mind was to accept either a `pathlib.Path` (which I try to use whenever handling file paths), or a string if, for some reason, the file path would get passed as one.

In my code was a function which looked something like
```python
from pathlib import Path
def func(file_list: Iterable[Filename]) -> list[Path]:
    # ...other stuff
    return list([Path(f) for f in file_list])

def calling_func() -> list[Path]:
    file_list = [Path("a"), Path("b")]
    try:
        new_var = func(file_list)
    except Exception:
        new_var = list(file_list)
    return new_var
```
That is, it would take an iterable of `Filenames` and produce a list of `Path`s. At some point, I realized that I wanted to have the output be the same type as the input (i.e. if I pass `str`s, return a list of `str`s; if I pass `Path`s, return a list of `Path`s).

When I changed the signature to
```python
def func(file_list: Iterable[Filename]) -> list[Path]:
    ...
```
`mypy` started complaining
```
error: Incompatible types in assignment (expression has type "List[Path]", variable has type "List[PathLike[str]]")
```

which would be triggered on this line:

```python HL:"6"
def calling_func() -> list[Path]:
    file_list = [Path("a"), Path("b")]
    try:
        new_var = func(file_list)
    except Exception:
        new_var = list(file_list)
    return new_var
```

I initially thought the problem was related to [Invariance vs. covariance](https://mypy.readthedocs.io/en/stable/common_issues.html#invariance-vs-covariance), my most commonly seen `mypy` error message when I am too specific with input types. My one-sentence summary of the problem is:
"`A <: B` (read: '`A` is a subtype of `B`')  does *not* imply that `list[A] <: list[B]` when `A,B` are invariant". However, changing everything to `Sequence` or `Tuple` did not fix the problem, as it does when Invariance is the root problem.

I realized that this could be solved by [making a "generic function" with `TypeVar`](https://mypy.readthedocs.io/en/stable/generics.html#generic-functions) like
```python
from typing import TypeVar
T = TypeVar('T')
def func(file_list: Iterable[T]) -> list[T]:
    ...
```
The problem with this is that it's *too* generic: I still want to constrain it to be `str` or `PathLike`.
But you can limit what types the `TypeVar` is able to be using either a list of specific types, or the `bound=` argument:
```python
PathLikeT = TypeVar('PathLikeT', bound=os.PathLike[str])
```
and then combine this with the [@overload decorator](https://docs.python.org/3/library/typing.html#overload) to describe multiple combinations of input/output types that a function can have:

```python
from typing import overload

@overload
def func(file_list: Iterable[str]) -> list[str]:
    ...  # literally just the ellipse here
    
@overload
def func(file_list: Iterable[PathLikeT]) -> list[PathLikeT]:
    ...


def func(file_list):
    # ...other stuff
    return list(file_list)
```

Now the typing system knows that the output container type will match that of the input, and that the function still only expects strings or `PathLike`s.