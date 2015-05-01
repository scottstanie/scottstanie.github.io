def fib():
    prev, cur = 0, 1
    while True:
        yield cur
        prev, cur = cur, prev + cur


def gen_perms(a):
    '''Generator to produce all permutations of a string or list
    Note that a[:i] + a[i+1:] removes the ith letter/ list item'''
    if len(a) == 1:
        yield a
    else:
        for i in range(len(a)):
            for perm in gen_perms(a[:i] + a[i+1:]):
                yield a[i:i+i] + perm


def generate_weights(weights, poss_weights):
    '''generator for an array of length n
    of all possible weights from -1 to 1
        weights: array of numbers, each slot has a set to choose from
        poss_weights: the set of weights to choose from
        cur_idx: the current indexo f the array that you are changing
        max_idx: the highest index that will change'''
    while max_idx < len(weights):
        yield weights
        weights[cur_idx] = poss_weights[cur_idx]


def main():
    poss_weights = [-1, 0, 1]
    w = 3  # 3 Potential weights to choose from
    n = 4  # Length of weight vector is 4
    # This means there are 3^4 = 243 permutations
    # to create for the weight vector
    weights = [poss_weights[0] for i in range(n)]
    print weights
    g = generate_weights(weights, 0)
    print list(g)
    f = fib()
    print list(f)

    p = permute_string('abcd')
    while True:
        try:
            print next(p)
        except StopIteration:
            break



if __name__ == '__main__':
    main()
