---
permalink: /til/always-show-defaults-in-click-cli-apps/
category: til
created: 2024-07-20T12:22
tags:
- python
- software
title: Always show defaults in click CLI apps
---

You can add [`show_default=True`](https://click.palletsprojects.com/en/latest/options/#basic-value-options) to any `@click.option` so that the `--help` message displays the defaults, but it seems like `click` has chosen not to include something as helpful as `argparse`'s [`ArgumentDefaultsHelpFormatter`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentDefaultsHelpFormatter), which aways shows the default. I remember searching for this a bunch of years back, but I finally came across a [satisfying patch:](https://github.com/pallets/click/issues/646#issuecomment-435317967)

```python
import click
click.option = functools.partial(click.option, show_default=True)
```



