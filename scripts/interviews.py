import math


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


def find_next_prime(p):
    '''Given prime p, return the next largest prime'''
    # Edge cases
    if p == 2:
        return 3
    if p % 2 == 0:
        return None

    # Test only up to the square root of the new prime
    lim = int(math.ceil(math.sqrt(p + 2)))

    found_flag = False

    # Test every odd
    p_next = p + 2

    while not found_flag:
        if all((p_next % i != 0) for i in xrange(2, lim + 1)):
            found_flag = True
            break
        p_next += 2

    return p_next


def nth_prime(n):
    '''Display the nth prime number'''
    primes = [2, 3]
    if n < 1:
        return 2
    elif n == 2:
        return 3

    while len(primes) < n:
        p = primes[-1]
        p_next = find_next_prime(p)
        primes.append(p_next)

    return primes[-1]


def euclids_iter(a, b):
    '''Euclid's algorithm for finding the GCD of two numbers
    Iterative method'''
    while b != 0:
        print a, b
        tmp = b
        b = a % b
        a = tmp
        print a, b
    return a


def euclids_recurse(a, b):
    '''Euclid's algorithm: recursive method'''
    if b == 0:
        return a
    else:
        return euclids_recurse(b, a % b)
