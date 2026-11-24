---
category: til
created: 2025-10-22T09:57
tags:
- python
- jax
- performance
- software
title: JAX has a great built-in profiler
---

After reminding myself that you need to add `.block_until_ready()` for timing purposes, or else [it just measures the dispatch time](https://docs.jax.dev/en/latest/async_dispatch.html#async-dispatch), I got to see that the function was entirely waiting on a "sort" XLA call.
By just inserting `with jax.profiler.trace("/tmp/jax-trace", create_perfetto_link=True):`, you can make this nifty profiler view:

{% include image.html url="/images/jax-perfetto-median.webp" alt="" %}

…which is how I found out that just switching from `median` to `mean` in a function can speed up results by 100x. All the code was waiting on a "sort"!

