---
title: 'Tree Algorithms'
layout: default
categories: [Tutorials, Random]
---

# Trees and Tree algorithms

Heaps and Binary search trees (BST) are two variations of a general binary tree. A binary tree is simply a linked data structure where each node is an object. Every node contains the attributes a *parent*, *left child*, and *right child*. The children may be null is the nodes are leaves of the tree, and the parent is null for the root. Heaps and BSTs are binary trees that have certain special ordering properties that make them useful.

## Binary Heaps

What is a binary heap? It is simply a binary tree that is:  
- ***Complete***: Every level is filled, except possibly the bottom (which gets filled in left to right)  
- ***Satisfies*** the *heap order property*, which means for a min/ max heap that every node is less/ greater than or equal to its children  

The heap order property leads to a few interesting characteristics:  
- The root node is always the smallest (largest for max heap)  
- Any path down a subtree is sorted, but different subtrees may not be sorted relative to each other (see below)  

<img src="http://i.imgur.com/tclAVS3.png" alt="Drawing" style="width: 300px;"/>
<img src="http://i.imgur.com/5goc4AX.png" alt="Drawing" style="width: 300px;"/>

## Priority Queues

To understand why we might use a binary head, let's examine what a **priority queue** is.
A *priority queue* is an abstract data type that is used in many different problems: essentially, anywhere that would require a queue, but also have a need to serve high priority items before lower priority items. Examples include operating systems, where jobs are scheduled according to priority, or doctors in the ER taking patients according to severity of injuries. It is first in first out (FIFO) similar to a queue, but high priority items are inserted near the front.  
Priority queues can be implemented with a heap, which have several advantages over other data structures which might be used. Below shows a table that outlines the run times of `find_min` and `insert` for these data structures:

 Data Structure| `insert` |  `find_min` 
|:---------------|:-----------:|----------:
List- sorted) | O(1) | O(n)  
List- unsorted) | O(n) | O(1))  
BST | O(log n) | O(log n))  
Heap | O(log n) | O(1)  

<br>
The BST (explored further below) option is good for different applications where all finds need to be quick. The Binary heap however is quicker when only `find_min` will be used.  

Another point about the binary heap is that it can be implemented using only an array.  Even though it is best visualized with a graph, no special node structure is needed. There are two reasons for this:  
- Each layer of the heap is ordered
- For each layer *i* (except the bottom) there will *always* be 2^i items

In the array, each layer will be a slice of size 2^i. The binary heap pictured above will look as follows in an array:

    H = [0, 5, 10, 94, 97, 24]

Finding the root simple: `H[1]`. The left and right child of node at index *i* will be located at \\(2\times i \\) and \\(2\times i + 1\\), respectively. This also means that the parent of node *i* is `i // 2`, where `//` denotes integer division.

### Heap Operations

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

Then, after popping the last item off the array and inserting it at the front, the function `percolate_down` might look like this:

    def percolate_down(self):
        idx = 1
        while idx * 2 < self.size:
            min_idx = self.min_child(idx)
            if self.heap_list[idx] > self.heap_list[min_idx]:
                self.swap_nodes(idx, min_idx)
            idx = min_idx

With these opearations to maintain the heap structure, implementing a priority queue is straightforward. 

## Binary search trees

What is a binary search tree? It is quite similar to a binary heap, with slightly different ordering of the nodes. The ***binary-search-tree*** property is the following: If x is a node in a BST, then for any node `r` in the right subtree of x and any node `l` in the left subtree, either \\(l <= x\\) or \\(r >= x\\)

This means ordering of a BST allows us to search through or print the node values quickly and in a simple recursive way.
### Tree Operations
To print the values of the tree in order, we use a function `in_order_walk` that looks like this:

    def in_order_walk(node):
      if node is not None:
        in_order_walk(node.left)
        print node
        in_order_walk(node.right)

#### Searching  
If we are looking for `k` in a BST `b`, the search algorithm looks like this:

    def search(node, k):
      if node is None or node == k:
        return node
      if x <= node:
        return search(node.left, k)
      else:
        return search(node.right, k)

If we call `search(b.root, k)`, the entire tree will be searched. The function only looks down half of the tree at each point, which means that it runs in O(log n). The above recursive procedure can also be rewritten iteratively:  

    def search(node, k):
      while node is not None and node != k:
        if node <= k:
          node = node.left
        else:
          node = node.right
      return node

This is usually more efficient than the recursive form.  
Finding the minimum and maximum of the tree is straightforward as well:

    def find_max(node):
      while node.left is not None:
        node = node.left
      return node

    def find_min(node):
      while node.right is not None:
        node = node.right
      return node

A *successor* of a node `x` is the smallest tree node with a key *greater* than `x.key`. To find this, we must consider the two cases of whether the right subtree of x is or is not null. The algorithm looks like this:

    def find_successor(x):
      if x.right is not None:
        return find_min(x)
      else:
        y = x.parent
        while y is not None and y.right == x:
          x = y
          y = x.parent
        return y

The case of a non-null right subtree is simple: the right child will be larger than `x`, so finding the minimum of the right subtree returns the minimum node greater than `x`.  
For the other case, we must traverse up the tree. The successor will appear as the first ancestor for which the current node is not the right child. If we take `y` as the parent and find that x is the left child (so `y.right != x`), this means that y is greater than x, and thus is the successor. If `y` becomes `None`, that means that there is no successor- the node is the largest in the tree.

#### Insertion

Inserting a new node `z` into the tree `T` requires us to traverse down the tree and insert it at some leaf.  

    def insert_node(T, z):
      x = T.root  # Start at the root
      y = None  # The leaf that we will insert under
      while x is not None:
        y = x
        if z.key < x.key:
          x = x.left
        else:
          x = x.right

        z.parent = y
        if y is None:
          T.root = z  # If the tree was empty

        if z.key < y.key:
          y.left = z
        else:
          y.right = z  

#### Deletion
For deleting a node `z` from a tree `T`, there are 3 basic cases to consider:
- `z` has no children: simply delete `z`
- `z` has one child: delete z and replace the z with the subtree of its child
- `z` has two children: First, find `y`, the successor of `z`, which will be in the right subtree. Then consider two subcases:
  - If the `y` is equal to the right child of `z`, just replace `z` right the subtree at `y`
  - Otherwise, move the `y` right child of to where `y` was located, then replace `z` with `y`

This last subcase must be considered because we need to merge the two subtrees in a way that preserves the binary search property.
