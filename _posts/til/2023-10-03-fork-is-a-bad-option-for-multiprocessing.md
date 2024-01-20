---
created: 2023-10-03 16:38:00
tags:
- software
- python
- parallel
title: '`fork` is a bad option for multiprocessing'
---

C.f. https://pythonspeed.com/articles/faster-multiprocessing-pickle/

Python's `multiprocessing` default option has been `fork()` when it is available. This might be the reason why I've had random crashes for different python version: If you have code which launches threads, then use a `fork()` operation, the code can freeze, deadlock or cause corrupted memory.

The child process resulting from `fork()` has all the data that was in memory for the parent, but it *doesn't copy any threads*. You can see this by running 

```python
import threading
from os import fork
from time import sleep

# Start a thread:
threading.Thread(target=lambda: sleep(60)).start()

if fork():
    print("The parent process has {} threads".format(
        len(threading.enumerate())))
else:
    print("The child process has {} threads".format(
        len(threading.enumerate())))
```
which will show `2 theads` for the parent and `1 threads` for the child.

The alternative is to use `spawn`, which doesn't copy anything over (and is described as "slower", but that seems like it shouldn't be an issue if your problem is large).
```python
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
# 1. 
ProcessPoolExecutor(max_workers=n, mp_context=multiprocessing.get_context("spawn"))
# 2. with Pool
with multiprocessing.get_context("spawn").Pool() as pool:
    ...
```
	
The downside is you'll need to make sure you copy everything you need to the other processes... but that should be explicit anyway.
