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


def cart_prod(out_idxs, cur_idx, choices):
    if cur_idx == 0:
        # To iterate through the choices in the tuple entry
        while out_idxs[cur_idx] < len(choices):
            yield [choices[i] for i in out_idxs]
            out_idxs[cur_idx] += 1

        out_idxs[0] = 0
        for it in cart_prod(out_idxs, cur_idx + 1, choices):
            yield it

    elif cur_idx < len(out_idxs):
        # Move the current choice index up one
        out_idxs[cur_idx] += 1
        if out_idxs[cur_idx] < len(choices):
            for it in cart_prod(out_idxs, 0, choices):
                yield it
        else:
            # Increment the current index and set all previous ones to 0
            out_idxs = [0 if i <= cur_idx else widx for i, widx in enumerate(out_idxs)]
            for it in cart_prod(out_idxs, cur_idx + 1, choices):
                yield it


def main():

    # [0, 0, 0, 0]
    tuple_length = 4
    out_idxs = [0 for i in range(tuple_length)]

    cur_idx = 0
    choices = ['a', 'b', 'c']

    gen = cart_prod(out_idxs, cur_idx, choices)
    ct = 0

    for g in gen:
        ct += 1
        print g, ct

if __name__ == '__main__':
    main()
