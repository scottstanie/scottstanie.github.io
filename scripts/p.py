
def gen(out_letters, out_idxs, poss_lets, cur_idx):
    if cur_idx == len(poss_lets):
        cur_idx = 0

    else:
        cur_idx += 1
        out_idxs[cur_idx]
    yield out_letters


def main():
    poss_lets = ['a', 'b', 'c']
    tuple_length = 4
    cur_idx = 0

    # ['a', 'a', 'a', 'a']
    out_letters = [poss_lets[0] for i in range(tuple_length)]

    # [0, 0, 0, 0]
    out_idxs = [0 for i in range(tuple_length)]

    break_word = [poss_lets[-1] for i in range(tuple_length)]

    while out_letters != break_word:
        out_letters = gen(out_letters, out_idxs, poss_lets, cur_idx)
        print out_letters
