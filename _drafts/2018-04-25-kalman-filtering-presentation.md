---
title: 'Beyond Kalman Filtering: Nonlinear Estimation Techniques'
layout: post
categories: articles
---
*This was adapted from a seminar-style talk I gave to my research group.*

This post gives an overview of the estimation problem statement, linear Estimation, a brief look at kalman Filtering, and maps out nonlinear extensions for more difficult problems.

## Estimation problem statement

The basic estimation problem looks like this (plur or minus different letters and notation):

$$ \mathbf{z}_k =  \mathbf{h}( \mathbf{x_k} , \mathbf{w_k}) $$

At a given time epoch k, We're given z as measurement of the true state x, which is corrupted by some noise w.

We usually get a set of measurements for some time before trying to estimate the true state:

$$  \mathbf{Z_k} = \left\lbrace z(1), z(2), \dots, z(k) \right\rbrace  $$

Our goal then is to create an **estimator**, a function of the measurements, that gives our best guess at what the real state \(x\) is.
We usually call this \( \hat{x}\).

$$ \mathbf{\hat{x}} =\mathbf{\hat{x}}(\mathbf{z}) $$

The class of problems can broadly be broken into **linear** or **nonlinear**, where linear problems looks like this:

$$ z = Hx + w $$

Matrix multiplications are always linear, which means that everything else is in the nonlinear category:

$$
 z = x^2 + w \\
 z = \arctan x + w \\
 z = x^3 w \\
 \ldots
$$

#### Approaches to estimation

The most common framesworks people use to solve estimation problems are:

- Ordinary least squares\* (OLS)
- Maximum Likelihood\* (ML)
- Maximum a-Posteriori\*\* (MAP)
- Minimum Mean Square Estimation\*\* (MMSE)

where \* are *non-Bayesian*, or *classical* techniques, while the two \*\* methods are **Bayesian**.

I'm assuming you are atleast somewhat familiar with some of the above techniques, so I'll just briefly define them.

EXPLAIN POSTERIOR, MAYBE MAKE SOME GRAPHS FOR THESE
Maximum Likelihood:

$$ \Lambda(x) = p(Z | x) $$

$$ \hat{x}\_{ML} = \arg \max_x \Lambda(x) $$

$$ \hat{x}\_{MAP} = \arg \max_x p(x|z) $$


The **MMSE** estimator is possibly the easiest to understand conceptually:

$$  \hat{x}\_{MMSE} = E[x | Z] $$


#### Static vs. Dynamic Estimation

Now that we have what the measurements and estimators might look like, what might our system, where x is coming from, look like?

**Static** system:

- The state x is not moving
- The problem is all about recovering x from the measurement noise w

Dynamic System:

- The state x is moving/changing with time
- There is still measurement noise from what we observe of x
- There can also be process noise
- We want estimates at each point in time

Note: While we can set up a static problem for a dynamical system if we only look at a single point in time.

SCREENSHOT HEIRARCHY OF PROBLEM

{% include image.html url="/images/kalman/pdfevolution.gif" height="340" width="640" %}
{% include image.html url="/images/kalman/pdfevolutionNoisy.gif" height="340" width="640" %}
{% include image.html url="/images/kalman/particleFilter2.gif" height="340" width="640" %}


## Linear Estimation


## Kalman Filtering


## Nonlinear Extensions
