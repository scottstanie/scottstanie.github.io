def find_sum_x(array, x):
    '''Given an unsorted array of integers,
    determing whether two numbers add up to x'''
    contains_sum = False

    # Assume that the sorting algorithm takes O(n lg(n)) time
    # e.g. merge sort, heapsort
    sorted_array = sorted(array)

    idx = 0
    jdx = len(sorted_array) - 1

    # The while loop will take O(n), as it loops once
    while idx != jdx and not contains_sum:
        if sorted_array[idx] + sorted_array[jdx] == x:
            contains_sum = True

        if sorted_array[idx] + sorted_array[jdx] < x:
            idx += 1

        if sorted_array[idx] + sorted_array[jdx] > x:
            jdx -= 1

    return contains_sum
