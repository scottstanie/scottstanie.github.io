import time

def binary_search_slice(alist, item):
    '''Sorts the list input and performs binary_search'''
    assert alist == sorted(alist), "Input list must be sorted"

    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return midpoint
        elif alist[midpoint] > item:
            return binary_search_slice(alist[:midpoint], item)
        else:
            return binary_search_slice(alist[midpoint + 1:], item)


def binary_search(alist, low, high, item):
    '''Sorts the list input and performs binary_search
    This implementation does not use the slice operator,
    and thus takes faster'''
    assert alist == sorted(alist), "Input list must be sorted"

    if low == high:
        return False
    else:
        midpoint = (low + high) // 2
        if alist[midpoint] == item:
            return midpoint
        elif alist[midpoint] > item:
            return binary_search(alist, low, midpoint, item)
        else:
            return binary_search(alist, midpoint + 1, high, item)


if __name__ == '__main__':
    alist = list(xrange(1000000))
    start_time = time.time()
    b1 = binary_search_slice(alist, 50000)
    print("---Slice binary search: %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    b2 = binary_search(alist, 0, len(alist) - 1, 50000)
    print("---No slice binary search: %s seconds ---" % (time.time() - start_time))
