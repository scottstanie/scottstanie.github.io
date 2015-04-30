# The Disjoin Set Data Structure

For some problems that require effeciency in memory or run time, solutions that involve Breadth First Search may be replaced with the disjoin set data structure.  
First, what is this data structure? It is simply a collection of disjoint sets \\(S_1, S_2, ... , S_n\\) that may be added to or removed from. Additionally, each set contains a *representative*, which is just some member from the set. For out examples, we will use the largest member. As a reminder, a set, informally, is just an *unordered* group of *unique* of things. Two sets are disjoint if they contain no members in common. E.g. \{1, 3, 4\} and \{2, 5\} are disjoint, but \{1, 3, 4\} and \{1, 5\} are not.  
To see how it might be use, let's look at an example scenario. Imaging there are a group of 5 of people hanging out called A, B, C, D, and E. At the start, \{A\}, \{B\}, \{C\}, \{D\}, \{E\} are all disjoint sets.  
Through the night, some become friends with each other, some do not. If A and B are friends \{A, B\} is now one of the disjoint sets, with \{C\}, \{D\}, \{E\} being the others. D and E become friends, which makes the sets \{A, B\}, \{D, E\}, and \{E\}. Finally, if B and D become friends, the two sets of two merge, so the final sets are \{A, B, D, E\}, and \{C\}.  
To check if two people are in the same group, we check their set representative. The representative of the set with person A is the same as that with E, so they are in the same set.  

We can define some functions for disjoint sets.

- `create_set(x)` - forms a set with one element, x
- `merge_sets(x,y)` - merges the set that contains x and that which contains y into one new set, destroying the old set
- `find_set(x)` - returns the representative of the set containing x

To set up our scenario using these functions, the code looks like this:

    # Gather the input of people in a list P [p1, p2, ... pn]
    for p in P:
      create_set(p)
    for (x, y) in friend_tuples:
      if find_set(x) != find_set(y):
        merge_sets(x, y)

Now we can just check `find_set(x) == find_set(y)` to see if `x` and `y` are friends.
