---
title: 'Beyond Kalman Filtering: Nonlinear Estimation Techniques'
layout: post
categories: articles
---
*This was adapted from a seminar-style talk I gave to my research group.*

This post gives an overview of the estimation problem statement, linear Estimation, a brief look at kalman Filtering, and maps out nonlinear extensions for more difficult problems.

## Estimation problem statement

The basic estimation problem looks like this (plus or minus different letters and notation):

$$ \mathbf{z}_k =  \mathbf{h}( \mathbf{x_k} , \mathbf{w_k}) $$

At a given time epoch k, We're given z as measurement of the true state x, which is corrupted by some noise w.

We usually get a set of measurements for some time before trying to estimate the true state:

$$  \mathbf{Z_k} = \left\lbrace z(1), z(2), \dots, z(k) \right\rbrace  $$

Our goal then is to create an **estimator**, a function of the measurements, that gives our best guess at what the real state \(x\) is.
We usually call this \\( \hat{x} \\) .

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


{% include image.html url="/images/kalman/estHierarchy.gif" height="340" width="640" %}
In the above diagram, "LTI" means "Linear, time invariant", as in the matrices F,H, and others are the same at every point in time.


Let's look are the solution to the basic static system with noise, \\( z = Hx + w\\)

$$
\hat{x} = \bar{x} + P_{xz} P_{zz}^{-1} (z - H \bar{x})
$$
Let's take it piece by piece.

The $\bar{x}$ is the "prior", the initial guess we have at what the state should be. 
It's a good idea to start there.

The $z - H \bar{x}$ term is called the "innovation".
z is the actual measurement we received, and $H \bar{x}$ is *what we think the measurement should have been$*.
We put our initial guess through the measurement model, compared it to the actual measurement, and the difference between them is new information.
Note that if that term were zero, if the measurement was exactly what we expected, there would be no added term to the prior and we would stick with that as our measurement.

The $ P\_{xz} $ term is the *covariance between the state and the measurement*.
Precisely, this cross covariance is $E[(x - E[x]) (z - E[z])^T].
A bigger terms means the measurement is *very related* to the state, so if we have a large innovation, we should update our estimate from the prior by a lot.

$ P\_{zz}$ is the covariance of the measurement, which is related to *how noisy the measurements are*.
A large value means it is noisy, and we can't trust the measurements very much.
Then $ P\_{zz}^{-1}$ can be thought of as the *information* of $z$.
A large $ P\_{zz}^{-1}$ comes from a small $ P\_{zz}$, which means the $z$ measurement gives us a lot of useful information and we can trust it a lot.
Small $ P\_{zz}^{-1}$ means theres not much good information in $z$, so even with a big change between what we expected and what we get, we shouldn't stray far from our prior.

In addition to the estimate, we can also look at the solution to the conditional covariance:

$$
P_{xx|z} = P_{xx} - P_{xz} P_{zz}^{-1} P\_{xz}^T
$$

This is the form of the best linear estimator.
It can also be derived from an MMSE approach.

In full form.
CREENSHOT.
{% include image.html url="/images/kalman/pdfEvolution.gif" height="340" width="640" %}
{% include image.html url="/images/kalman/pdfEvolutionNoisy.gif" height="340" width="640" %}
{% include image.html url="/images/kalman/particleFilter2.gif" height="340" width="640" %}


## Linear Estimation


## Kalman Filtering


## Nonlinear Extensions
