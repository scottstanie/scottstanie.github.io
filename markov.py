import argparse
import collections
import random
import string


class Markov(object):

    def __init__(self, open_file, lookback=3):
        self.lookback = lookback
        self.cache = collections.defaultdict(list)
        self.open_file = open_file
        self.words = self.file_to_words()
        self.word_size = len(self.words)
        self.database()

    def file_to_words(self):
        self.open_file.seek(0)
        data = self.open_file.read()
        words = self.clean_text(data)
        return words.split()

    def clean_text(self, text):
        # Remove non-ascii characters
        text = filter(lambda x: x in string.printable, text)

        # Remove links the might have been posted
        wordlist = filter(lambda x: 'http' not in x, text.split(' '))

        # Get rid of random periods
        wordlist = [w for w in wordlist if w != '.']

        # Remove newlines and rejoin the words into one string
        return ' '.join(wordlist).replace('\n', '')

    def ntuples(self):
        """ Generates n-tuples from the given data string. So if our string were
                "What a lovely day" and n=3, we'd generate (What, a, lovely) and then
                (a, lovely, day).
        """

        if len(self.words) < self.lookback:
            return

        for i in range(len(self.words) - (self.lookback - 1)):
            yield tuple(self.words[i:i + self.lookback])

    def database(self):
        for words in self.ntuples():
            key = tuple(words[:self.lookback - 1])
            self.cache[key].append(words[self.lookback - 1])

    def generate_markov_text(self, size=25):
        seed = random.randint(0, self.word_size - self.lookback)
        seed_words = self.words[seed:seed + self.lookback - 1]
        gen_words = []
        for i in xrange(size):
            gen_words.append(seed_words[0])
            seed_words = seed_words[1:] + [random.choice(self.cache[tuple(seed_words)])]
        gen_words.extend(seed_words[1:])
        return ' '.join(gen_words)


if __name__ == '__main__':
    '''Usage:
        python markov.py <size of text to generate>'''
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-file', help='Input text file')
    parser.add_argument(
        '--lookback', default='3', help='Number of words for the \
                Markov chain to look back'
    )
    parser.add_argument('--output', help='Number of words to output')
    args = parser.parse_args()
    markovgen = Markov(open(args.input_file), int(args.lookback))
    print 'Reading from %s:' % args.input_file
    print markovgen.generate_markov_text(size=int(args.output))
