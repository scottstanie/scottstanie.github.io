import math


def kadane(A):
    '''A non recursive, linear time algo for finding
    the maximum subarray.
    Returns the (min index, max index, sum) of the subarray'''

    current_max = 0  # For keeping track of the latest non-zero sum
    total_max = 0  # The global max sum
    ci_min = ti_min = ti_max = 0

    for idx in range(len(A)):
        print 'A[idx]', A[idx]
        if current_max + A[idx] > 0:
            current_max = current_max + A[idx]
        else:
            current_max = 0
            ci_min = idx + 1 if idx + 1 < len(A) else idx

        if current_max > total_max:
            print current_max
            print total_max
            print '---'
            total_max = current_max
            ti_min = ci_min
            ti_max = idx

    return ti_min, ti_max, total_max


def find_max_crossing_subarray(A, low, mid, high):
    '''Finds the max sub array that crosses the midpoint
    Loops from the mid down, and mid up to find two separate max arrays
    that end at the midpoint. The total max subarray will be the
    sum of these two arrays'''

    c_i = c_j = mid  # Start total indices at the mid and expand outward
    max_low = 0
    for idx in range(mid, 0, -1):
        if sum(A[idx:mid + 1]) > max_low:  # the slice to mid + 1 will include A[mid]
            max_low = sum(A[idx:mid + 1])
            c_i = idx

    max_high = 0
    for jdx in range(mid + 1, high):
        if sum(A[mid + 1:jdx]) > max_high:
            max_high = sum(A[mid + 1:jdx])
            c_j = jdx - 1

    c_sum = max_low + max_high
    return c_i, c_j, c_sum


def div_conquer(A, low, high):
    '''Recursive, divide and conquer method for max subarray finding
    Returns (min index, max index, sum) of the subarray'''
    if low == high:
        return low, high, A[low]
    else:
        mid = int(math.floor((low + high) / 2))
        llow, lhigh, lsum = div_conquer(A, low, mid)
        rlow, rhigh, rsum = div_conquer(A, mid + 1, high)
        clow, chigh, csum = find_max_crossing_subarray(A, low, mid, high)

        if lsum > rsum and lsum > csum:
            return llow, lhigh, lsum
        elif rsum > lsum and rsum > csum:
            return rlow, rhigh, rsum
        else:
            return clow, chigh, csum


if __name__ == '__main__':
    A = [4, -2, -8, 5, -2, 7, 7, 2, -6, 5]
    print 'A: ', A
    dc = div_conquer(A, 0, len(A) - 1)
    print dc
    print A[dc[0]:dc[1]]
    k = kadane(A)
    print k
    print A[k[0]:k[1]]
