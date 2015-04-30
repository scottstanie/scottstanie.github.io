# Dynamic Programming

As a Dynamic Program (DP) is a technique based on a recurrence formula in which solutions are formed from previously found sub solutions. An example is probably the best way to see what this means.

#### The coins problem
The classic exmaple of a dynamic programming problem is finding the minimum number of coins required to make a certain amount of change. Let's say you want you need to pay someone 39 cents with standard U.S. coins and want to use the fewest number possible.  
The simplest way to figure out how to do this is with a ***greedy algorithm***. In this case, you would start with the largest coin and count until it would go over, then move to the next largest, and down until you make the correct amount. Here that would be 1 quarter + 1 dime + 4 pennies.  
This is optimal for the case of normal U.S. coins. But what if we had a coint that was 13 cents? The greedy algorithm would fail to see that we can do it in 3 coins.  
How would we find this optimal solution? We construct a dynamic program. To do so, we start with a recurrent formula. This involves finding a *state* which we know the optimal solution to, then using that to find the solution to the next largest state.  
For example, if we know what coin assortment is the best solution to making 12 cents, we can use that to find the optimal solution to 13 cents but just adding one more penny.
