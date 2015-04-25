# A Graph is a set G = {V, E} consistint of edges and vertices.
# Graphs can be directed or undirected.
# Order: the number of vertices in a graph
# Size: the number of edges in the graph
#
# First example of a graph: a single linked list
import numpy as np


class List_node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Linked_list(object):
    def __init__(self):
        self.nodes = []
        self.head = None

    def print_list(self):
        cur = self.nodes[0]
        print 'head:'
        while cur.next is not None:
            print cur.data
            cur = cur.next
        print cur.data

    @staticmethod
    def cost(a, b):
        '''The cost of reaching b from a'''
        if a.next == b:
            return 1
        elif a == b:
            return 0
        else:
            return "Not possible"


class Tree_node(object):
    '''For a family tree'''
    def __init__(self):
        self.mother = None
        self.father = None
        self.name = None


class Tree(object):
    '''Tree must be a connect acyclic graph'''
    def __init__(object):
        self.root = None

    @staticmethod
    def cost(a, b):
        if a.mother == b or a.father == b:
            return 1
        elif a == b:
            return 0
        else:
            return "Not possible"


class Graph_node(object):
    def __init__(self):
        self.neighbors = []
        self.data


class Graph(object):
    '''General Graph class using Graph_nodes'''
    def __init__(self, nodes=[]):
        super(Graph, self).__init__()
        self.nodes = nodes

    @staticmethod
    def cost(a, b):
        if b in a.neighbors:
            # Return the number of edges from a to b
            return len((item for item in a.neighbors if item == b))


class Graph_matrix(object):
    def __init__(self, matrix=None):
        super(Graph_matrix, self).__init__()
        self.matrix = matrix


class Stack(object):
    """Stack in python"""
    def __init__(self, items=[]):
        super(Stack, self).__init__()
        self.items = items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        p = self.items.pop()
        return p

    def top(self):
        if not self.empty():
            return self.items[-1]
        else:
            return None

    def empty(self):
        return not self.items


if __name__ == '__main__':
    a = List_node(1)
    b = List_node(2)
    c = List_node(3)
    a.next = b
    b.next = c
    c.next = None
    ll = Linked_list()
    ll.nodes = [a, b, c]
    ll.print_list()
