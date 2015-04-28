---
title: 'Tree Algorithms'
layout: default
---

# Priority Queues and Binary Heaps

A priority queue is an abstract data type that is used in many different problems: essentially, anywhere that would require a queue, but also have a need to serve high priority items before lower priority items. Examples include operating systems, where jobs are scheduled according to priority, or doctors in the ER taking patients according to severity of injuries. It is first in first out (FIFO) similar to a queue, but high priority items are inserted near the front.  
Priority queues can be implemented with a binary heap. These have several advantages over other data structures which might be used. Below shows a table that outlines the run times of `find_min` and `insert` for these data structures:

 Data Structure| `insert` |  `find_min` 
|:---------------|:-----------:|----------:
List- sorted) | O(1) | O(n)  
List- unsorted) | O(n) | O(1))  
Binary Search Tree (BST) | O(log n) | O(log n))  
Binary Heap | O(log n) | O(1)  

<br>
The Binary Search Tree option is good for different applications where all finds need to be quick. The Binary heap however is quicker when only `find_min` will be used.  
What is a binary heap? It is simply a binary tree that is:  
- Complete: Every level is filled, except possibly the bottom (which gets filled in left to right)  
- Satisfies the *heap order property*, which means for a min/ max heap that every node is less/ greater than or equal to its children  

The heap order property leads to a few interesting characteristics:  
- The root node is always the smallest (largest for max heap)  
- Any path down a subtree is sorted, but different subtrees may not be sorted relative to each other (see below)  

<img src="http://i.imgur.com/tclAVS3.png" alt="Drawing" style="width: 300px;"/>
<img src="http://i.imgur.com/5goc4AX.png" alt="Drawing" style="width: 300px;"/>

Another interesting point about the binary heap is that it can be implemented using only an array.  Even though it is best visualized with a graph, no special node struct is needed. There are two reasons for this:  
- Each layer of the heap is ordered
- For each layer *i* (except the bottom) there will *always* be 2^i items

In the array, each layer will be a slice of size 2^i. The binary heap pictured above will look as follows in an array:

    B = [0, 5, 10, 94, 97, 24]

Finding the root simple: `B[1]`. The left and right child of node at index *i* will be located at \\(2\times i \\) and \\(2\times i + 1\\), respectively. This also means that the parent of node *i* is `i // 2`, where `//` denotes integer division.



