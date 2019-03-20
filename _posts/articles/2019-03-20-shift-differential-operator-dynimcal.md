---
title: 'Connecting the Shift and Differential Operator to Dynamical Systems'
layout: post
categories: articles
---

I recently came across a podcast called [My favorite Theorem](https://kpknudson.com/my-favorite-theorem/), which is great for math nerds.
Each show they bring one professor to talk about something from math they like
(ideally, their favorite math theorem, although sometimes this only lasts 5 minutes).

The professor in the latest episode began talking about his theorem, which didn't have a name,
and in fact was so short that he described it in about 3 sentences.
The theorem goes like this:


>> Let f(x) be a single variable function.
If we call call \$D\$ be the differential operator:
>>
$$ Df(x) = \frac{df}{dx}  $$
>>
and call the "shift" operator E:  
>>
$$ Ef(x) = f(x+1) $$
>>
>> then  
>>
$$ e^{D} = E. $$
>>
>> That is exponentiating the differential operator is equivalent to the shift operator.

Despite the simplicity, he pointed out it was his favorite because it has given
many engineering students he's taught a big "aha" moment, and I definitely in that category.

It's relatively easy prove (as far as math theorems go).
To clarify what $e^D$ means, we will use the same definition that makes \$e^x\$
sensible for both imaginary numbers and for matrices: the Taylor series expansion:

$$
e^D = 1 + D + \frac{D^2}{2!} + \frac{D^3}{3!} + \ldots
$$  

Here, \$D^2\$ means applying the D operator two times in a row,
\$D^2 = \frac{d^2f}{dx^2} = f^{\'\'}(x)\$,
a.k.a. the second derivative.

Now the only thing left to the proof is recognizing that \$e^D f(x)\$
is already the Taylor series expansion of \$f(x + 1)\$ in disguise.

Since the expansion of a function \$g(y)\$ is at the point \$a\$:

$$
g(y) = g(a) + g^{ ' }(a)(y-a) + \frac{g^{' '}(a)}{2} (y-a)^2
$$

this means if we Taylor expand \$f(x + 1) \$ and substitute \$x\$ for \$a\$, \$(x+1)\$ for \$y\$, we get

$$
E f(x) = f(x + 1) \\
= f(x) + f^{ ' }(x)[(x+1)-x] + \frac{f^{' '}(x)}{2} [(x+1)-x]^2 \\
= f(x) + f^{ ' }(x) + \frac{f^{' '}(x)}{2} \\
= e^D f(x)
$$


## Connection to stable dynamical systems

This fact is weird and unexpected on its own, but it also has a great connection
to material taught in dynamical systems classes.
We're usually taught two ideas about when continuous time systems and
discrete time systems are stable, and rarely given a good reason why they should connect.

A system is stable if, as time goes on indefinitely, the value of \$x\$ will never
blow up to infinity.
For continuous time system, with \$x\$ is being a scalar function of \$t$:

$$
\frac{dx}{dt} = A x(t)
$$

the system is stable if \$A\$ has real part less than 0, \$Re(A) < 0\$.
The stable region for this system \$A\$ is **in the left half of the complex plane**:
Alternatively, if \$x\$ is a vector and \$A\$ a matrix, the eigenvalues of \$A\$ must all
  have real parts less than zero and all be in the left half of the plane.


Once discrete systems are introduced:

$$
x[k+1] = A x[k]
$$

stability occurs if the magnitude of A (which could be complex),
is less than one (or, if A is a matrix, the eigenvalues all must have
  magnitude less than one).
So the stable region for this system is **within the unit circle**.

How do these connect?
Well, sometimes the justification is just to solve each of these differential equations
and see what they look like:
The continuous time solution looks like \$k e^{At}\$, so any real part above
zero makes this go to infinity as \$t \rightarrow \infty \$.
Likewise, you solve the discrete version by repeatedly multiplying the starting
\$x[0]\$ by \$A\$ until you get something like \$x[n] = A^n x[0] \$.
Thus, an \$A\$ that has absolute value above 1 will go to infinity as n grows.

However, I think the theorem gives a much more satisfying connection between
these two systems.
We see that the *evolution* of the continuous system (that is, how it moves from
  one time instant to the next), is given by the **differential operator** \$D\$:

$$
Dx(t) = \frac{dx}{dt} = Ax(t)
$$

while the discrete system moves forward from the **shift operator** \$E\$:

$$
Ex[k] = x[k+1] = A x[k]
$$

Once we see this, we can guess how we might connect the stable region of the
continuous time system to the discrete one: **exponentiate it**!

Using [3blue1brown plotting library, manim](https://github.com/scottstanie/manim),
we can visualize this this in the nicest way possible by taking every point
in the plane \$a + bi \$ and transforming it to \$ e^{a + bi}\$:

{% include image.html url="/images/lhp_animation.gif" description="Demonstration with manim [1]" height="420" width="600" %}


Thus, all stable points that evolve by the \$D\$ operator are in the same
region as stable points that evolve by the \$E\$ operator once they're exponentiated.  
