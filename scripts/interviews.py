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


###### TOWER OF HANOI ########
class Pole(object):
    def __init__(self, num_rings, name=""):
        self.letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
        self.rings = self.letters[:num_rings]
        self.name = name
        self.num_rings = len(self.rings)

    def __str__(self):
        return self.name + ' [' + ', '.join(item for item in self.rings) + ']'


class Tower(object):
    def __init__(self, num_rings=1):
        self.from_pole = Pole(num_rings, 'from_pole')
        self.to_pole = Pole(0, 'to_pole')
        self.with_pole = Pole(0, 'with_pole')
        self.total_moves = 0

    def __str__(self):
        return str(self.from_pole) + '\n' + str(self.with_pole) + '\n' + str(self.to_pole)

    def move_tower(self, num_rings, from_pole, to_pole, with_pole):
        if num_rings < 2:
            self.move_disk(from_pole, to_pole)
        else:
            self.move_tower(num_rings - 1, from_pole, with_pole, to_pole)
            self.move_disk(from_pole, to_pole)
            self.move_tower(num_rings - 1, with_pole, to_pole, from_pole)

    def move_disk(self, fp, tp):
        print 'Moving disk from ' + str(fp) + ' to ' + str(tp)
        d = fp.rings.pop()
        tp.rings.append(d)
        print self
        self.total_moves += 1



if __name__ == '__main__':
    tow = Tower(4)
    print tow
    tow.move_tower(tow.from_pole.num_rings, tow.from_pole, tow.to_pole, tow.with_pole)
    print 'Total moves: ', tow.total_moves
