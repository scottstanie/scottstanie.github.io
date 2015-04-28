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
- ***Complete***: Every level is filled, except possibly the bottom (which gets filled in left to right)  
- ***Satisfies*** the *heap order property*, which means for a min/ max heap that every node is less/ greater than or equal to its children  

The heap order property leads to a few interesting characteristics:  
- The root node is always the smallest (largest for max heap)  
- Any path down a subtree is sorted, but different subtrees may not be sorted relative to each other (see below)  

<img src="http://i.imgur.com/tclAVS3.png" alt="Drawing" style="width: 300px;"/>
<img src="http://i.imgur.com/5goc4AX.png" alt="Drawing" style="width: 300px;"/>

Another interesting point about the binary heap is that it can be implemented using only an array.  Even though it is best visualized with a graph, no special node struct is needed. There are two reasons for this:  
- Each layer of the heap is ordered
- For each layer *i* (except the bottom) there will *always* be 2^i items

In the array, each layer will be a slice of size 2^i. The binary heap pictured above will look as follows in an array:

    H = [0, 5, 10, 94, 97, 24]

Finding the root simple: `H[1]`. The left and right child of node at index *i* will be located at \\(2\times i \\) and \\(2\times i + 1\\), respectively. This also means that the parent of node *i* is `i // 2`, where `//` denotes integer division.

#### Heap Operations

Clearly finding the min is easy (`H[1]`). What about inserting into the heap? The obvious first step would be appending to the end of the list. This would maintain the *complete* property of the heap, but probably not maintain the well ordered property. Therefore, we must *percolate up* the new node until it fits satisfies the ordering property.  
This really just involves comparing the inserted node to each of its parents up the subtree until one is found that is smaller. We can use the division techniques described about. So, for inserting `7` into the array H above the percolation steps are:  
    
    # Index of 7 is 6 -> the parent is index 6 // 2 = 3
    H = [0, 5, 10, 94, 97, 24, 7]
    
    # 94 > 7, swap the two entries. 
    H = [0, 5, 10, 7, 97, 24, 94]

    # Check new parent index at 3 // 2 = 1
    # H[1] = 5, and 5 <= 7, so the heap order is satisfied
    H = [0, 5, 10, 7, 97, 24, 94]

This can be coded as:

    def percolate_up(H, idx):
        while idx > 0:
            if H[idx] > H[idx // 2]:
                # Swap parent and child nodes
                H[idx], H[idx // 2] = H[idx // 2], H[idx]

            idx = idx // 2
    

The run time of this insertion is \\(log(n) \\) due to the divisions by 2.  
What about deleting the min node at the top of the heap? What we can do is replace it with the last item in the list, then create a procedure similar to the previous one to restore the heap order. First, we make a helper function to find the index of the smaller of a node's two children:

    def min_child(self, idx):
        '''Returns the index of the minimum child of the node
        at idx.'''
        # If there are not two children, return the index of the left child
        if 2*idx + 1 > self.size:
            return idx * 2
        else:
            # Check the right child first
            if self.heap_list[idx] < self.heap_list[2*idx + 1]:
                return 2*idx
            else:
                return 2*idx + 1

Then, the function `percolate_down` might look like this:

    def percolate_down(self):
        idx = 1
        while idx * 2 < self.size:
            min_idx = self.min_child(idx)
            if self.heap_list[idx] > self.heap_list[min_idx]:
                self.swap_nodes(idx, min_idx)
            idx = min_idx
