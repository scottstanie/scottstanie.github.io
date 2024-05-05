---
created: 2024-04-21T18:48
tags:
- python
- parallel
- llms
title: imap_unordered needs to have its Pool open
---

If you have a situation where you're trying to process in parallel many tasks with Python and
1. their processing times may vary greatly
2. you want to work with the results as soon as they get in
then [`multiprocessing.imap`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.imap) may be good options. If, in addition, you don't care about the order they get processed and returned in, you can use [`imap_unordered`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.imap_unordered)

For a simple demonstration, let's pretend we have 20 tasks, each taking somewhere between 1 and 4 seconds to complete.

```python
import multiprocessing as mp
import random
import time


def process(tup):
    idx, sec = tup
    time.sleep(sec)
    print(f"Worker {idx} done in {sec} seconds")
    return idx


def test_imap_unordered():
    tasks = [(i, random.randint(1, 4)) for i in range(20)]

    with mp.Pool(8) as pool:
        results = pool.imap_unordered(process, tasks)

        for r in results:
            print(f"Done with worker {r}")


if __name__ == "__main__":
    test_imap_unordered()

```

A benefit of these asynchronous iterators comes if the inputs to your processing function are large and you don't want to hold all of them in memory (as would occur if you used `multiprocessing.map`, which converts your input iterator to a `list`). 

However, a subtle issue can occur if you change the indentation above to 
```python
    with mp.Pool(8) as pool:
        results = pool.imap_unordered(process, tasks)

	for r in results:
		print(f"Done with worker {r}")
```
This looks inoccuous enough, especially if you're used to using `pool.map(...)`.  However, the `results` object is an [`IMapIterator`](https://github.com/python/cpython/blob/6d87cb494ba27ef5c2a4a59240a7ed792bb0bcce/Lib/multiprocessing/pool.py#L415) which lazily works through the outputs as they come in. When an output is finished and consumed, it signals to the pool to process the next input.

The problem: When we exit the context manager block, the inputs stop getting processed. This causes a deadlock: Nothing will actually get processed in the version where you dedent the `for r in results`.


This subtle issue was pointed out to me by [Claude 3 Opus](https://www.anthropic.com/claude). I'm recording this question and answer because this feels like another noticeably jump in performance of LLMs: Two very smart and experienced developers were looking at the code and didn't see what the issue was. While I'm sure they could have eventually figured it out, I solved the problem in < 5 minutes by asking the question with [the `llm` command line tool](https://github.com/simonw/llm) (reformatting for clarity):

```
$ llm chat -m claude-3-opus
Chatting with claude-3-opus-20240229
Type 'exit' or 'quit' to exit
Type '!multi' to enter multiple lines, then '!end' to finish
> !multi
```

>  I have some python code where the multiprocessing is hanging ONLY with imap_unordered:
 ```python
 # Create a pool and dispatch
 with Pool(processes=worker_count, maxtasksperchild=1) as p:
	 # mp_tasks = p.map(wrap_solve_mcf, uw_inputs(range(nruns)))  # runs fine!
	 mp_tasks = p.imap_unordered(wrap_solve_mcf, uw_inputs(range(nruns))) # FAILS!

 # runs fine!
 # p = Pool(processes=worker_count, maxtasksperchild=1)
 # mp_tasks = p.imap_unordered(wrap_solve_mcf, uw_inputs(range(nruns)))
 # p.close()

```
> Why is that? what is different?


The answer from Claude:

<details>

The difference between `map` and `imap_unordered` is in how they return the results and how the main process interacts with the worker processes.

1. `map`:
   - `map` blocks until all the tasks are completed and returns the results as a list in the same order as the input iterable.
   - The main process waits for all the worker processes to finish before proceeding.
   - It is suitable when you need all the results at once and in a specific order.

2. `imap_unordered`:
   - `imap_unordered` returns an iterator that yields the results as soon as they are available, in an arbitrary order.
   - The main process can start processing the results as they become available, without waiting for all the tasks to complete.
   - It is suitable when you don't need the results in a specific order and want to start processing them as soon as possible.

The issue with your code using `imap_unordered` is likely related to the fact that you are using a `with` statement to manage the pool. When the `with` block ends, the pool is automatically closed and joined, which means the main process waits for all the worker processes to finish.

However, with `imap_unordered`, the main process needs to actively consume the results from the iterator returned by `imap_unordered`. If you don't consume the results, the worker processes may hang waiting for the main process to retrieve the results.

To fix the issue, you can consume the results from the iterator returned by `imap_unordered`. Here's an example:

```python
with Pool(processes=worker_count, maxtasksperchild=1) as p:
    mp_tasks = p.imap_unordered(wrap_solve_mcf, uw_inputs(range(nruns)))
    results = list(mp_tasks)  # Consume the results from the iterator
```

By converting the iterator returned by `imap_unordered` to a list using `list(mp_tasks)`, you actively consume the results, allowing the worker processes to complete and the pool to be properly closed and joined.

Alternatively, you can use the commented-out code that you mentioned, where you manually manage the pool without using a `with` statement:

```python
p = Pool(processes=worker_count, maxtasksperchild=1)
mp_tasks = p.imap_unordered(wrap_solve_mcf, uw_inputs(range(nruns)))
results = list(mp_tasks)  # Consume the results from the iterator
p.close()
```

In this case, you explicitly close the pool after consuming the results from the iterator.

Remember to handle the results appropriately based on your requirements, whether you need them in a specific order or not.


</details>

Shockingly coherent and helpful.
