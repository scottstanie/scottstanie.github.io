import random


class Bg(object):
    def __init__(self, size=4, max_int=3):
        self.tiles = [[random.randint(0, max_int) for idx in range(size)] for idx in range(size)]

    def __str__(self):
        s = ''
        for row in self.tiles:
            s += ', '.join(str(i) for i in row) + '\n'
        return s

    def __repr__(self):
        return self.__str__()

    def find_neighbors(self, r, c, new):

        up = (r - 1, c) if r > 0 else (None, None)
        down = (r + 1, c) if r < 3 else (None, None)
        right = (r, c + 1) if c < 3 else (None, None)
        left = (r, c - 1) if c > 0 else (None, None)

        dirs = [up, left, down, right]

        n = []
        for tr, tc in dirs:
            if tr is not None and tc is not None and self.tiles[tr][tc] == new:
                n.append((tr, tc))
        return n

    def flood_recurse(self, r, c, old, new):
        '''Recursive method to flood_recurse tiles'''
        if old == new:
            return
        if old != self.tiles[r][c]:
            return
        self.tiles[r][c] = new

        n = self.find_neighbors(r, c, old)
        for nr, nc in n:
            self.flood_recurse(nr, nc, old, new)

    def move_recurse(self, new):
        self.flood_recurse(0, 0, self.tiles[0][0], new)

    def move_BFS(self, new):
        visited = {}  # Make has of (r, c) coordinates
        to_visit = [(0, 0)]
        old = self.tiles[0][0]

        while to_visit:
            cur_r, cur_c = to_visit.pop(0)
            visited[(cur_r, cur_c)] = 1
            self.tiles[cur_r][cur_c] = new

            # Find all neighbors in boundary with same color
            n = self.find_neighbors(cur_r, cur_c, old)

            # Only use unvisited neighbors
            n = [neigh for neigh in n if not visited.get(neigh)]
            to_visit.extend(n)

    def win(self):
        '''Check if the tiles are the same = player has won'''
        cur = self.tiles[0][0]  # Use any tile to check if they all match
        return all((item == cur for row in self.tiles for item in row))


if __name__ == '__main__':
    # Recursive method call- just keep trying
    bg = Bg()
    print 'START'
    print bg

    win_flag = False
    while not win_flag:
        for r in range(4):
            for c in range(4):
                bg.move_recurse(bg.tiles[r][c])
                win_flag = bg.win()

    print 'END'
    print bg

    # Using the move_BFS method  method
    bg2 = Bg()
    print 'START'

    print bg2

    win_flag = False
    while not win_flag:
        for r in range(4):
            for c in range(4):
                bg.move_BFS(bg.tiles[r][c])
                win_flag = bg.win()

    print 'END'
    print bg
