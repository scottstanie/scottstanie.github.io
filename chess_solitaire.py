# Solves the 4x4 Chess Solitaire problem:
'''Consider the game of Solitaire Chess, which is played on a
4x4 chess board with an arbitrary number of pieces, all of the same color.
To win, a player must eliminate all pieces on the board, save for one.
To accomplish this, he may make any sequence of legal chess moves,
subject to the additional constraint that every move must result in a capture.
Pawns may move from the top to the bottom:

. . N .
. . . .
. P . .
B Q . R

N is a Knight,
B is a Bishop,
P is a Pawn,
Q is a Queen,
the R is a Rook (in the general case,
we might also have K's for Kings).

This board can be solved with the following sequence of moves:

Step 1:  Rook takes Queen

. . N .
. . . .
. P . .
B R . .

Step 2:  Rook takes Pawn

. . N .
. . . .
. R . .
B . . .

Step 3:  Bishop takes Rook

. . N .
. . . .
. B . .
. . . .

Step 4:  Knight takes Bishop

. . . .
. . . .
. N . .
. . . .

A more challenging example:

. . N .
B P . .
N B R .
. . R P

The problem is to take an arbitrary chess board as input
and generate all solutions, if available, or output 'no solution'.
The solvable boards should output all solutions as above.

This solution uses a tuple to represent the board configuration.
For example,

. . N .
. . . .
. P . .
B R . .

becomes

(0, 0, N, 0,
 0, 0, 0, 0,
 0, P, 0, 0,
 B, R, 0, 0 )

A look at the indices of the board reveals how pieces can move:
(
0 , 1 , 2 , 3 ,
4 , 5 , 6 , 7 ,
8 , 9 , 10, 11,
12, 13, 14, 15
)

The letters will be classes in the tuple, where each piece class
can calculate the legal moves it has available.
In the tuple scheme, the moves are calculated by position index jumps:

P: at position 9, it can move to 12 or 14 (diagonally). It cannot move up.
    Therefore, P has at most position +3 or position + 5 as legal.
    Of course, this assumes that P + 3 or P + 5 has a piece in that position,
    (if if is 0, then it is not a capture and not a legal move)
    and that it does not move off the board- can't move +3 on
    indices where (idx % 4 == 0), and can't move +5 on spots
    where (idx+1 % 4 == 0).

R: Simply idx +/1 for horizontal, and idx +/-4 for vertical
    Restrictions:
    R = idx + 1 : (idx-3) % 4 != 0
    L = idx - 1 : idx % 4 != 0
    D = idx + 4 : idx < 12
    U = idx - 4 : idx > 3

B: Diagonal movement = idx +/- 3 or idx +/-5
    Restrictions:
    idx + 3 : idx < 12 and idx % 4 != 0
    idx + 5 : idx < 12 and idx-3 % 4 != 0
    idx - 3 : idx < 12 and idx-3 % 4 != 0
    idx - 5 : idx < 12 and idx % 4 != 0

N: Knight is the most complicated for calculating moves.
    Assuming Down=D, R=Right, L=Left, U=Up:

    +/-9 (DDR, UUL), +/-7 (DDL, UUR), +/-6 (DRR, ULL), +/-2 (DLL, URR)
    Restrictions on Knight moves:
    All DD* : idx < 8
    All UU* : idx > 7
    All LL* : (idx % 4 != 0) and ((idx-1) % 4 != 0)
        This means it can't be in the left two columns
    All RR* : ((idx-2) % 4 != 0) and ((idx-3) % 4 != 0)

    Additionally, the last letter must account for
        the top, left, bottom and right most edges:
    **R : ((idx-3) % 4 != 0)
    **L : ((idx) % 4 != 0)
    **U : idx > 3
    **D : idx < 12


The solution will use a Breadth First Search (BFS), representing
each board state as a node on the graph. The funtion find_next(board)
will calculate all possible next board configurations.
These next possible configurations are listed as neighbors for the node
and pushed onto a queue to be searched.
Visited boards are marked
'''
from collections import deque


class Piece(object):
    '''Abstract Piece to be subclasses
    pos = position index on the board
    has methods to check for various movements'''
    def __init__(self, pos=None):
        super(Piece, self).__init__()
        self.pos = pos
        self.letter = None

    def __str__(self):
        return self.letter

    def __repr__(self):
        return self.letter

    def chk_ul(self, pos):
        return self.chk_u(pos) and self.chk_l(pos)

    def chk_ur(self, pos):
        return self.chk_u(pos) and self.chk_r(pos)

    def chk_dl(self, pos):
        return self.chk_d(pos) and self.chk_l(pos)

    def chk_dr(self, pos):
        return self.chk_d(pos) and self.chk_r(pos)


    @staticmethod
    # Check if it can move up
    def chk_d(pos):
        return pos < 12

    def chk_u(pos):
        return pos > 3

    def chk_l(pos):
        return pos % 4 != 0

    def chk_r(pos):
        return (pos - 3) % 4 != 0


class Pawn(Piece):
    def __init__(self, *args):
        super(Pawn, self).__init__(*args)
        self.letter = 'P'
        self.my_moves = [
            (3, self.chk_r),
            (5, self.chk_l),
            ]

    def __str__(self):
        return 'P'

    def __repr__(self):
        return 'P'


class Knight(Piece):
    def __init__(self, *args):
        super(Knight, self).__init__(*args)
        self.letter = 'K'
            # [UUL, UUR, ULL, URR, DLL, DRR, DDL, DDR]
        self.my_moves = [
            (-9, self.chk_uul),
            (-7, self.chk_uur),
            (-6, self.chk_ull),
            (-2, self.chk_urr),
            (2, self.chk_dll),
            (6, self.chk_drr),
            (7, self.chk_ddl),
            (9, self.chk_ddr),
        ]

    def chk_uul(self):
        return self.chk_uu() and self.chk_l()

    def chk_uur(self):
        return self.chk_uu() and self.chk_r()

    def chk_ull(self):
        return self.chk_u() and self.chk_ll()

    def chk_urr(self):
        return self.chk_u() and self.chk_rr()

    def chk_dll(self):
        return self.chk_d() and self.chk_ll()

    def chk_drr(self):
        return self.chk_d() and self.chk_rr()

    def chk_ddl(self):
        return self.chk_dd() and self.chk_l()

    def chk_ddr(self):
        return self.chk_dd() and self.chk_r()

    @staticmethod
    # Knight specific movement checks
    def chk_dd(pos):
        return pos > 8

    def chk_uu(pos):
        return pos < 7

    def chk_ll(pos):
        return (pos.pos % 4 != 0) and ((pos - 1) % 4 != 0)

    def chk_rr(pos):
        return ((pos - 2) % 4 != 0) and ((pos - 3) % 4 != 0)


class Bishop(Piece):
    def __init__(self, *args):
        super(Bishop, self).__init__(*args)
        self.letter = 'B'
        self.my_moves = [
            (-5, self.chk_ul),
            (-3, self.chk_ur),
            (3, self.chk_dl),
            (5, self.chk_dr),
        ]


class Rook(Piece):
    def __init__(self, *args):
        super(Rook, self).__init__(*args)
        self.letter = 'R'
        self.my_moves = [
            (-4, self.chk_u),
            (-1, self.chk_l),
            (1, self.chk_r),
            (4, self.chk_d),
        ]


class Queen(Rook, Bishop):
    def __init__(self, *args):
        super(Queen, self).__init__(*args)
        self.letter = 'Q'
        self.my_moves = [
            (-5, self.chk_ul),
            (-4, self.chk_u),
            (-3, self.chk_ur),
            (-1, self.chk_l),
            (1, self.chk_r),
            (3, self.chk_dl),
            (4, self.chk_d),
            (5, self.chk_dr),
        ]


class Board_state(object):
    '''Class to represent the nodes on the graph'''
    def __init__(
            self,
            pieces=(0, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0, 0,),
            neighbors=[],
            parent=None,
            visited=False):
        self.pieces = pieces
        self.neighbors = neighbors
        self.visited = visited
        self.string_form = self.stringify()
        self.stringify()
        self.winner = False  # Used to trace paths of winners

        # self.initialize_pieces()

    def stringify(self):
        '''Visualize board state'''
        all_str = ''
        for row_idx in range(4):
            row = self.pieces[4*row_idx: 4*(row_idx + 1)]
            str_row = ' '.join(str(item) for item in row)
            all_str += str_row + '\n'

        return all_str

    def __str__(self):
        return self.string_form

    def initialize_pieces(self):
        '''Returns non zero pieces and sets their index pos'''
        p_idx = [(idx, piece) for idx, piece in enumerate(self.pieces)]

        new_pieces = []
        for i, p in p_idx:
            if p:
                p.pos = i
            new_pieces.append(p)

        self.pieces = tuple(new_pieces)
        self.string_form = self.stringify()

    def find_all_captures(self, visited):
        '''Loop through pieces of board, find available next moves'''
        pieces = [piece for piece in self.pieces if piece]
        # piece_indices = [idx for idx, p in enumerate(self.pieces) if p]
        # print 'piece_indices for me ', piece_indices
        new_boards = []

        for piece in pieces:
            # Find the captures available- a list of new positions
            capture_positions = self.find_capture(piece)
            for idx in piece.next_positions():
                if idx in piece_indices and idx != piece.pos:
                    print 'piece is: ', piece
                    print 'pieces next position ', idx
                    new_pieces = self.capture(piece, idx, piece.pos)
                    b = Board_state(pieces=new_pieces)
                    b.initialize_pieces()
                    # if not visited.get(b.string_form):
                    new_boards.append(b)
                        # Mark as visited by storing in hash
                        # visited[b] = 1
                    b.parent = self

        # print 'new boards'
        # for b in new_boards:
            # print b
        # print '---'
        return new_boards

    def capture(self, piece_to_move, capture_pos, old_pos):
        '''If there is a capture, return pieces for a new Board_state'''
        new_pieces = list(self.pieces)
        piece_to_move.pos = capture_pos
        new_pieces[capture_pos] = piece_to_move
        new_pieces[old_pos] = 0
        return tuple(new_pieces)

    def find_capture(self, piece):
        # Check all legal directions with their checking function
        legal_dirs = [(move, chk_func) for move, chk_func in piece.my_moves if piece.chk_func(piece.pos)]
        cur_pos = piece.pos

        capture_positions = []
        for direc, chk_func in legal_dirs:
            capture_flag = False
            one_move_flag = False
            # Keep moving until there is a capture or a boundary
            while not capture_flag and not one_move_flag and piece.chk_func(cur_pos):
                if self.pieces[cur_pos + direc]:
                    capture_flag = True
                    capture_positions.append(cur_pos + direc)
                cur_pos += direc
                if piece.letter in ('N', 'P'):  # Pawns and knight only move once
                    one_move_flag = True

        return capture_positions




if __name__ == '__main__':
    q = Queen()
    r = Rook()
    p = Pawn()
    # print q.my_moves
    # print 'position: ', q.pos
    # print q.allowed_moves()
    pieces = (
            0, q, 0, 0,
            0, p, r, 0,
            0, 0, 0, 0,
            0, 0, 0, 0,)
    b = Board_state(pieces=pieces)
    b.initialize_pieces()
    print 'START'
    print '------'

    qu = deque()
    qu.append(b)

    visited = {}
    iter_num = 1
    while len(qu) > 0:
        print '{} Boards in the queue'.format(len(qu))
        print 'Running this board: '
        cur = qu.popleft()
        print cur
        new_boards = cur.find_all_captures(visited)
        qu.extend(new_boards)
        # print visited
        print 'ITERATION NUMBER {}'.format(iter_num)
        iter_num += 1
        if iter_num == 100:
            break

