import re


def double(string):
    return string + string


def addu(string):
    if string.endswith('i'):
        return string + 'u'


def i_to_u(string):
    """Use a lookahead to find overlapping starts of iii,
        change them to u"""
    for match in re.finditer(r'(?=iii)', string):
        yield string[:match.start()] + 'u' + string[match.start() + 3:]


def cut_us(string):
    """Use lookahead to find overlapping starts of uu and cut
    """
    for match in re.finditer(r'(?=uu)', string):
        yield string[:match.start()] + string[match.start() + 2:]


if __name__ == '__main__':
    start = 'i'
    attempted = set()
    moves = ['i']
    while True:
        try:
            current = moves.pop()
        except IndexError:
            print 'No moves left'
            break

        if current in attempted:
            continue

        if current == 'u':
            print 'DONE!'
            break

        attempted.add(current)
        s1 = double(current)
        if len(s1) < 20:
            moves.append(s1)
        s2 = addu(current)
        if s2 and len(s2) < 20:
            moves.append(s2)
        for move in i_to_u(current):
            moves.append(move)
        for move in cut_us(current):
            moves.append(move)

    print len(attempted), 'attempted'
