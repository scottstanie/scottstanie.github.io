class Heap(object):
    def __init__(self):
        self.heap_list = [0]
        self.size = 0

    def __repr__(self):
        return 'Heap list: ' + ', '.join(str(i) for i in self.heap_list)

    def get_size(self):
        return self.size

    def swap_nodes(self, idx, jdx):
        self.heap_list[idx], self.heap_list[jdx] = \
                    self.heap_list[jdx], self.heap_list[idx]

    def percolate_up(self, idx):
        while idx > 0:
            if self.heap_list[idx] < self.heap_list[idx // 2]:
                self.swap_nodes(idx, idx // 2)

            idx = idx // 2

    def insert(self, item):
        self.heap_list.append(item)
        print 'before percolate', self.heap_list
        self.size += 1
        self.percolate_up(self.size)

    def percolate_down(self):
        idx = 1
        while idx * 2 < self.size:
            min_idx = self.min_child(idx)
            if self.heap_list[idx] > self.heap_list[min_idx]:
                self.swap_nodes(idx, min_idx)
            idx = min_idx

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

    def delete_min(self):
        '''Removes the min node, then percolates down to restore heap'''
        self.swap_nodes(1, self.size)
        p = self.heap_list.pop()
        self.size -= 1
        print 'Removing ', p
        self.percolate_down()



def percolate_down():
    idx = 1
    while idx * 2 < size:
        min_idx = min_child(idx)
        if heap_list[idx] > heap_list[min_idx]:
            swap_nodes(idx, min_idx)
        idx = min_idx

def min_child(idx):
    '''Returns the index of the minimum child of the node
    at idx.'''
    # If there are not two children, return the index of the left child
    if 2*idx + 1 > size:
        return idx * 2
    else:
        # Check the right child first
        if heap_list[idx] < heap_list[2*idx + 1]:
            return 2*idx
        else:
            return 2*idx + 1

if __name__ == '__main__':
    h = Heap()
    h.insert(3)
    print h
    h.insert(5)
    print h
    h.insert(7)
    print h
    h.insert(1)
    print h
    h.insert(2)
    print h
    h.insert(10)
    print h

    h.delete_min()
    print h

