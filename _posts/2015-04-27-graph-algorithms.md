---
title: 'Graphs in python.'
layout: default
---
# Graphs in python

## Depth First Search

Sketch of algorithm:

```
1. Start with a node to search from, and mark it as 'searched'
2. Visit one of the neighboring nodes and mark it
3. Visit some neighbor node until there are none you haven't visited, then go to next neighbor node from (2)
4. Continue until all are marked
```


## Breadth First Search

Sketch of algorithm:

Before proving the various properties of breadth-first search, we take on the somewhat easier job of analyzing its running time on an input graph G D = (V;E). We use aggregate analysis, as we saw in Section 17.1. After initialization, breadth-first search never whitens a vertex, and thus the test in line 13 ensures that each vertex is enqueued at most once, and hence dequeued at most once. The operations of enqueuing and dequeuing take O(1) time, and so the total time devoted to queue operations is O(V)). Because the procedure scans the adjacency list of each vertex only when the vertex is dequeued, it scans each adjacency list at most once. Since the sum of the lengths of all the adjacency lists is \theta(E), the total time spent in scanning adjacency lists is O(E). The overhead for initialization is O(V), and thus the total running time of the BFS procedure is O(V + E). Thus, breadth-first search runs in time linear in the size of the adjacency-list representation of G.
