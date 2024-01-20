---
created: 2023-10-18 16:36:00
tags:
- software
- performance
- python
- tools
title: Airspeed Velocity
---

## Benchmarking with `asv`

Airspeed Velocity ([`asv`](https://asv.readthedocs.io/en/v0.6.1/)) seems to be the best existing way to run a few benchmarks and get progress over time. It's used by `numpy`, `pandas`, `scikit-image`, `xarray`, and a few others. Pandas even seems to have spent time/money to set up a "collection" of benchmarks here: https://asv-runner.github.io/asv-collection/pandas/ 

### Basics

1. Install with `pip`, run `asf quickstart` to make a template `asv.conf.json` (which you need to fill out)
2. Run `asv machine` or `asv machine --yes` to have it save info about the computer you are about to run things on
3. (After writing your benchmarks) Run benchmarks with `asv run`
	- This will install the environment that you specified, which will be reused.
4. Compile the results with `asv publish`

### Naming the benchmark tests

The benchmarks almost look like normal `pytest` or `UnitTest` files, except all the names have `time_` or `mem_` as the function names... And that's because `asv` will use that to figure out what it's tracking
- `time_<blah>` will run a function (and call the result whatever you've named this function). and measure the *time*

### Using it in CI

You can run against a specific git commit, or a tag, like 
```
asv run v0.1^!
```
Getting some version to run the benchmark in Github actions seems not too hard,  and there's an even nicer way to do this on Github using PR labels([1]) 

{% raw %}
```yaml
on:
  pull_request:
    types: [labeled]

jobs:
  benchmark:
    if: ${{ github.event.label.name == 'run-benchmark' && github.event_name == 'pull_request' }}
```
{% endraw %}

This lets you label a PR with `run-benchmark` and have it trigger the workflow, which I think is very nice.

Also during this investigation, I saw that you can run Github Actions on a [timer like a cronjob](https://github.com/jaimergp/scikit-image/blob/e561996df7daa3d7164326c5c29cc6898c32518f/.github/workflows/benchmarks-cron.yml#L3-L7)
It's called the [`schedule` event to trigger a workflow](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule).

### Running the benchmarks on every tagged release

`asv run` accepts multiple ways to specify commits to run the benchmarks on. The common ones people use are something like `HEAD~1...HEAD`,
But you can also pass a list of specific hashes... So we can use the command `git show-ref --tags` to list all the tagged commits
```bash
git show-ref --tags --hash > hashlist.txt
```
then pass this to `asv run`:
```bash
asv run HASHFILE:tagged_commits.txt
```

### Skipping commits that we've already benchmarked
Using the `--skip-existing-commits`, you could theoretically run 
```
asv run --skip-existing-commits ALL
```
every time, and it would only take a really long time once.

### Using it on a giant server with many CPUs
If you don't want to use all the cores available to the benchmarks, you can specify `--cpu-affinity 0-8` when we only want it to use 8 CPUs. This is key for running the benchmarks on our 224 CPU cluster when the production code may only have 8 or 16 cores.

### How do we save the results? 

There seem to be many ways to save the resulting data points, but scikit-image seems to use the Github Artifacts to store data. They actually made a [custom jupyter notebook to download and parse the artifacts](https://gist.github.com/jaimergp/aa4f059c14e394c4089b320cb8b51b1a) to write up the report on whether it was useful to test their code on the Github Actions machines.


### More examples in the wild
- [TQDM has a longer workflow with it](https://github.com/tqdm/tqdm/blob/4c956c20b83be4312460fc0c4812eeb3fef5e7df/.github/workflows/check.yml#L26)
- [scikit-image](https://github.com/scikit-image/scikit-image/blob/12be1553f2d439fe997052293b3fe8fcdf69f6f6/.github/workflows/benchmarks.yml) has a regular version, but also [a cron version](https://github.com/jaimergp/scikit-image/blob/e561996df7daa3d7164326c5c29cc6898c32518f/.github/workflows/benchmarks-cron.yml#L3-L7)
- [Scipy has docs about it here](https://docs.scipy.org/doc/scipy/dev/contributor/benchmarking.html) and their [graphs are up here](https://pv.github.io/scipy-bench/)
- [scikit-learn has a separate repo setup](https://github.com/scikit-learn/scikit-learn-benchmarks)
- [Sarsen has a simple setup](https://github.com/bopen/sarsen-benchmarks/blob/main/.github/workflows/benchmark-and-deploy.yml), but they've put semi-real data into git LFS... which is probably why it's in a separate repo
- [napari has a complicated GHA setup](https://github.com/Czaki/napari/blob/1b1baa8291ff03fb7732b9ca27b33ef471da0b71/.github/workflows/benchmarks.yml)
## References

1. https://labs.quansight.org/blog/2021/08/github-actions-benchmarks