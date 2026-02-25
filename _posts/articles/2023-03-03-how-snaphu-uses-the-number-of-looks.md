---
category: articles
created: 2023-03-03 08:48:00
has_math: 'true'
tags:
- insar
- phase-unwrapping
title: How SNAPHU uses the number of looks
---

Varying the number of looks parameter in SNAPHU has a surprisingly large effect on the output, especially the connected component output. Why is that?

SNAPHU uses correlation in two places; both are simple equations, but I can't actually map them to a single equation in the provided reference (Touzi, 1999).

1. Calculate a $\rho_0$:

$$
\rho_0 = \frac{c_1}{L} + c_2
$$
where $c_1 = 1.3, c_2 = 0.14$ are constants (whose defaults in SNAPHU I'm using here) and $L$ is the number of looks (probably the [effective number of SAR looks]()).

2. Using $\rho_{0}$, compute a low correlation threshold (from [full configuration manual](https://web.stanford.edu/group/radar/softwareandlinks/sw/snaphu/snaphu.conf.full))

> Values smaller than the threshold `rhominfactor`*`rho0` are assumed to
> come from zero statistical correlation because of estimator bias (double).

So using the [default in isce3's snaphu](https://github.com/isce-framework/isce3/blob/07633f1d35757346f431a697ab442b629e47de51/python/packages/isce3/unwrap/snaphu.py#L536) `min_corr_factor=1.25`, correlation values smaller than
$$
1.25 \cdot (\frac{c_1}{L} + c_2)
$$
are assumed to indicate pixels which contain pure noise. Here's what this threshold is for looks up to 50:

{% include image.html url="/images/How SNAPHU treats correlation and looks-1677852084283.jpeg" alt="|1/2" %}

So we see that if your correlation value hits 0.2, SNAPHU is treating it as equal to 0 correlation.


## Example
My go-to for weird unwrapping things is the UAVSAR Sacramento Delta example:
{% include image.html url="/images/How SNAPHU treats correlation and looks-1677852321426.jpeg" alt="None" %}
This is the phase, correlation, and histogram of correlation.

Unwrapping the interferogram with `looks` ranging from 5 to 50 gives this:
{% include image.html url="/images/How SNAPHU treats correlation and looks-1677852443267.jpeg" alt="None" %}

If we use the curve above to see which regions are ignored as 0 correlation for different input look numbers:
{% include image.html url="/images/How SNAPHU treats correlation and looks-1677852216529.jpeg" alt="None" %}

Comparing the two, it's not obvious where you'll get connected components just from looking at the masked regions. 
Worse still, you would have no chance of guessing where the connected components will be placed from the unwrapped phase alone (which looks mostly the same for all 5 cases).



