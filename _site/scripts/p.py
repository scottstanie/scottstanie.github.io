
def iter_letter(out_idxs, cur_idx, poss_lets, break_cond):
    if out_idxs == break_cond:
        print 'finished'
        yield False
    if cur_idx == 0:
        # To iterate through the choices in the tuple entry
        while out_idxs[cur_idx] < len(poss_lets):
            yield [poss_lets[i] for i in out_idxs]
            out_idxs[cur_idx] += 1

        out_idxs[0] = 0
        for it in iter_letter(out_idxs, cur_idx + 1, poss_lets, break_cond):
            yield it

    elif cur_idx < len(out_idxs):
        out_idxs[cur_idx] += 1
        # Move the current choice index up one
        if out_idxs[cur_idx] < len(poss_lets):
            for it in iter_letter(out_idxs, cur_idx - 1, poss_lets, break_cond):
                yield it
        else:
            # Increment the current index and set all previous ones to 0
            out_idxs = [0 if i < cur_idx + 1 else widx for i, widx in enumerate(out_idxs)]
            for it in iter_letter(out_idxs, cur_idx + 1, poss_lets, break_cond):
                yield it


def get_let_index(letter):
    return let_index[letter]


def main():

    # choices = [1, 2, 3]
    # let_index = dict((item, idx) for idx, item in enumerate(poss_lets))

    # tuple_length = 4

    # # ['a', 'a', 'a', 'a']
    # out_letters = [poss_lets[0] for i in range(tuple_length)]

    # # [0, 0, 0, 0]
    # out_idxs = [0 for i in range(tuple_length)]

    # break_word = [poss_lets[-1] for i in range(tuple_length)]

    out_idxs = [0, 0, 0, 0]
    cur_idx = 0
    poss_lets = ['a', 'b', 'c']
    break_cond = [2, 2, 2, 2]

    dd = iter_letter(out_idxs, cur_idx, poss_lets, break_cond)
    ct = 0
    for d in dd:
        ct += 1
        print d, ct

    print ct

if __name__ == '__main__':

    main()
