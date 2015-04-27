import random


def insertion_sort(A):
    '''Input A of numbers, size n.
        Sort in increasing order with insertion sort'''

    for j in range(1, len(A)):
        key = A[j]

        # Insert A[j] into sorted sequence A[1..j-1]
        i = j - 1
        swap_count = 0
        while i > -1 and A[i] > key:
            # print "A[i + 1]", A[i + 1]
            # print "A[i]", A[i]
            A[i + 1] = A[i]
            i -= 1
            swap_count += 1
        print 'key = ', key
        print 'swap_count = ', swap_count
        A[i + 1] = key
        print 'new array: ', A, '\n'

    return A


def insertion_sort_right_to_left(A):
    '''Same algo as insert, but left to right '''
    N = len(A) - 1      # Last index of Array is len(A) - 1
    # Now start a second from the right, and work left
    for j in range(N - 1, -1, -1):
        key = A[j]

        # Insert A[j] to the right into sorted A[j..N]
        i = j + 1
        swap_count = 0
        while i <= N and key > A[i]:
            A[i - 1] = A[i]
            i += 1
        print 'key = ', key
        print 'swap_count = ', swap_count
        A[i - 1] = key
        print 'new array: ', A, '\n'

    return A


def non_increasing_insertion_sort(A):
    '''Same algo, now non increaing'''

    for j in range(1, len(A)):
        key = A[j]

        # Insert A[j] into sorted sequence A[1..j-1]
        i = j - 1
        swap_count = 0
        while i > -1 and A[i] < key:
            # print "A[i + 1]", A[i + 1]
            # print "A[i]", A[i]
            A[i + 1] = A[i]
            i -= 1
            swap_count += 1
        print 'key = ', key
        print 'swap_count = ', swap_count
        A[i + 1] = key
        print 'new array: ', A, '\n'


def bubble_sort(A):
    '''Implement bubblesort on the list A'''
    for passnum in xrange(len(A) - 1, 0, -1):
        for idx in xrange(passnum):
            if A[idx] > A[idx + 1]:
                A[idx], A[idx + 1] = A[idx + 1], A[idx]


def selection_sort(alist):
    '''Same idea as bubblesort, but only one swap per loop iteration'''
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        alist[fillslot], alist[positionOfMax] = alist[positionOfMax], alist[fillslot]

if __name__ == '__main__':

    # A = random.sample(xrange(10), 10)
    A = [random.randint(0, 10) for x in xrange(10)]
    print 'A before the sort: ', A, '\n'

    # A = insertion_sort(A)
    # A = non_increasing_insertion_sort(A)
    selection_sort(A)
    print 'A after the sort: ', A
