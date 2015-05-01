from itertools import islice

def gen(letters, word, x):
    print 'x', x
    while True:
        yield [letters[word[i]] for i in range(len(word))]

        word_check = [len(letters)-1 for i in range(4)]
        if word == word_check:
            yield False
            break;

        elif x < len(word) and word[x] < len(letters) - 1:
            print 'elif'
            word[x] += 1

        else:
            print 'x', x
            print 'else'
            word[x] = 0
            x += 1

def main():
    letters = ['a', 'b', 'c']
    word = [0 for i in range(4)]
    x = 0
    f = gen(letters, word, x)
    while True:
        try:
            w = f.next()
            print w
        except StopIteration:
            print 'done'
            break

main()
