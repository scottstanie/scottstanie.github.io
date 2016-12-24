---
title: 'Sorting algorithms.'
layout: post
categories: random
redirect_from:
- /random/2015/04/14/sorting/algorithms
- /blog/2015/04/14/sorting/algorithms
---
# Insertion Sort

Start with sequence of keys < a<sub>1</sub>, a<sub>2</sub>, \.\.\. ,a<sub>n</sub> >

The insertion sort algorithm in python looks like the following:


	for j in range(1, len(A)):
		key = A[j]
		# Insert A[j] into sorted sequence A[0..j-1]
		i = j - 1
		while i >= -1 and A[i] > key:
			A[i + 1] = A[i]
			i -= 1
		A[i + 1] = key

	return A

Explained briefly, the algorithm will look at each item starting with the second, compare it to all items that come before it (lower index, to the left), move each item to the left once over, and stop once either the beginning of the array is reached or the current key is greater than the item to the left.

### Loop invariant
At each itertion of j, the array `A[0..j-1]` consists of the elements originally in the posisions 0 through j-1, but now in sorted order.  
There are three points to show about a loop invariant to prove it is correct:

- **Initialization**: It is true prior to the first iteration of the loop
- **Maintenance**: If it is true before an iteration, it remains true after
- **Termination**: When a loop terminates, the invariant gives us a useful property that helps show the algorithm is correct

The Initialization and Maintenance properties are similar to the base case and inductive step of mathematical induction.

In the insertion sort example: 

- **Initialization**: Prior to the first iteration, A[0..j-1] = A[0], which is trivially sorted
- **Maintenance**: Each iteration, the loop inner i loop will move A[j-1], A[j-2], ... to the right until the correct place for A[j] is found. After incrementing j, the loop invariant holds.
- **Termination**: When the loop terminates, this means that j has reached the end of A. Since the loop invariant holds during each iteration, we now have all of A sorted.


## Big O Analysis of Insertion Sort

To study the running times of insertion sort, we must define the input size and which running time we mean. Most cases, input size means the number of items in the input- in this case, the array of size n. When multiplying two integers, the total number of bits needed to represent the input is the input size.  
Running Time is usually measured in primitive \"steps\" to make it machine indepedent. Analysis can consist of looking at:
- Worst case run time: theta of n
- Average case: big-O
- Best case:

Worst case is often used when you either want to know the upper bound of run time, or realistically the algorithm's worst case may appear often (e.g. a database search algorithm where the item is not present).  


# Merge Sort

Merge sort is the first example of a *divide and conquer* algorithm. This is in contrast to the *incremental* algorithm of insertion sort. In that case, we had A[1..j-1] sorted, and just inserted A[j] into its proper place.  
Divide and conquer algorithms have three stages:
- **Divide** the problem into smaller instances of the same problem
- **Conquer** the subproblems by solving recursively. Once they are small enough, solve in a straightforward manner.
- **Combine** the solutions into the overall olution

In merge sort, the steps are:
- Divide the n-element sequence into two subsequences
- Conquer each subsequence using merge sort
- Merge the two sorted subsequences into one sorted answer


# Quick Sort

Another divide and conquer algorithm.

    def quick_sort(A, low, high):
        if low < high:
            splitpoint = partition(A, low, high)
            quick_sort(A, low, splitpoint - 1)
            quick_sort(A, splitpoint + 1, high)


    def partition(A, low, high):
        '''Find new split point for quick sort'''
        pivot = A[low]
        left = low
        right = high

        found = False  # Search for new split point
        while not found:
            while left <= right and A[left] <= pivot:
                left += 1

            while left <= right and A[right] >= pivot:
                right -= 1

            if right < left:
                found = True
            else:
                A[left], A[right] = A[right], A[left]

        # Insert pivot to correct place and return new splitpoint
        A[low], A[right] = A[right], A[low]
        return right
