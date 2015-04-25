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
These next possible configurations are children of the node
and pushed onto a queue to be searched.
'''
from collections import deque
import copy


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

    # Check if it can move up
    def chk_d(self, pos):
        return pos < 12

    def chk_u(self, pos):
        return pos > 3

    def chk_l(self, pos):
        return pos % 4 != 0

    def chk_r(self, pos):
        return (pos - 3) % 4 != 0

    def chk_ul(self, pos):
        return self.chk_u(pos) and self.chk_l(pos)

    def chk_ur(self, pos):
        return self.chk_u(pos) and self.chk_r(pos)

    def chk_dl(self, pos):
        return self.chk_d(pos) and self.chk_l(pos)

    def chk_dr(self, pos):
        return self.chk_d(pos) and self.chk_r(pos)


class Pawn(Piece):
    def __init__(self, *args):
        super(Pawn, self).__init__(*args)
        self.letter = 'P'
        self.my_moves = [
            (3, self.chk_dl),
            (5, self.chk_dr),
            ]

    def __str__(self):
        return 'P'

    def __repr__(self):
        return 'P'


class Knight(Piece):
    def __init__(self, *args):
        super(Knight, self).__init__(*args)
        self.letter = 'N'
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

    def chk_dd(self, pos):
        return pos < 8

    def chk_uu(self, pos):
        return pos > 7

    def chk_ll(self, pos):
        return (pos % 4 != 0) and ((pos - 1) % 4 != 0)

    def chk_rr(self, pos):
        return ((pos - 2) % 4 != 0) and ((pos - 3) % 4 != 0)

    def chk_uul(self, pos):
        return self.chk_uu(pos) and self.chk_l(pos)

    def chk_uur(self, pos):
        return self.chk_uu(pos) and self.chk_r(pos)

    def chk_ull(self, pos):
        return self.chk_u(pos) and self.chk_ll(pos)

    def chk_urr(self, pos):
        return self.chk_u(pos) and self.chk_rr(pos)

    def chk_dll(self, pos):
        return self.chk_d(pos) and self.chk_ll(pos)

    def chk_drr(self, pos):
        return self.chk_d(pos) and self.chk_rr(pos)

    def chk_ddl(self, pos):
        return self.chk_dd(pos) and self.chk_l(pos)

    def chk_ddr(self, pos):
        return self.chk_dd(pos) and self.chk_r(pos)


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
            parent=None):
        self.pieces = pieces
        self.neighbors = neighbors
        self.parent = parent
        self.string_form = self.stringify()
        self.stringify()
        self.win_paths = []  # Used to trace paths of winners

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

    def size(self):
        return len([p for p in self.pieces if p])

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

    def find_all_captures(self):
        '''Loop through pieces of board, find available next moves'''
        pieces = [piece for piece in self.pieces if piece]
        # piece_indices = [idx for idx, p in enumerate(self.pieces) if p]
        # print 'piece_indices for me ', piece_indices
        new_boards = []

        for piece in pieces:
            # Find the captures available- a list of new positions
            capture_positions = self.find_capture(piece)
            for cap_pos in capture_positions:
                new_pieces = self.capture(piece, cap_pos, piece.pos)
                b = Board_state(pieces=new_pieces)
                b.initialize_pieces()
                b.parent = self
                new_boards.append(b)

        return new_boards

    def find_capture(self, piece):
        # Check all legal directions with their checking function
        legal_dirs = [(move, chk_func) for move, chk_func in piece.my_moves if chk_func(piece.pos)]
        capture_positions = []
        for direc, chk_func in legal_dirs:
            cur_pos = piece.pos  # Reset to the original position
            capture_flag = False
            one_move_flag = False  # Pawns and knight only move once

            # Keep moving until there is a capture or a boundary
            while not capture_flag and not one_move_flag and chk_func(cur_pos):
                if self.pieces[cur_pos + direc]:
                    capture_flag = True
                    capture_positions.append(cur_pos + direc)
                cur_pos += direc
                if piece.letter in ('N', 'P'):
                    one_move_flag = True

        return capture_positions

    def capture(self, piece_to_move, capture_pos, old_pos):
        '''If there is a capture, return pieces for a new Board_state'''
        new_pieces = list(self.pieces)
        piece_copy = copy.deepcopy(piece_to_move)
        piece_copy.pos = capture_pos
        new_pieces[capture_pos] = piece_copy
        new_pieces[old_pos] = 0
        return tuple(new_pieces)


def run_BFS(start_board, queue):
    queue.append(start_board)

    all_boards = []
    win_idx = 0

    while len(queue) > 0:
        cur = queue.popleft()
        all_boards.append(cur)

        # DEBUG: print each board through the queue
        # print 'Running this board: '
        # print cur

        if cur.size() > 1:
            new_boards = cur.find_all_captures()
            queue.extend(new_boards)
        else:
            cur.win_paths.append(win_idx)
            win_idx += 1

    num_strategies = win_idx

    return all_boards, num_strategies


def find_path(cur_board, path_num):
    if cur_board.parent:
        cur_board.parent.win_paths.append(path_num)
        find_path(cur_board.parent, path_num)


def print_winners(all_boards, num_strategies):
    print '------'
    print 'WINNING PATHS:'
    print '------'

    for win_idx in range(num_strategies):
        print 'Strategy Number {}'.format(win_idx + 1)
        for b in all_boards:
            if win_idx in b.win_paths:
                print b

        print '-------'


def main():
    q = Queen()
    r = Rook()
    p = Pawn()
    n = Knight()

    pieces = (
            0, 0, 0, 0,
            r, 0, 0, q,
            0, 0, p, 0,
            0, n, 0, 0,)
    start_board = Board_state(pieces=pieces)
    start_board.initialize_pieces()

    print 'START_board'
    print '------'
    print start_board

    queue = deque()

    all_boards, num_strategies = run_BFS(start_board, queue)

    all_winners = [board for board in all_boards if board.win_paths]

    # Trace back along the graph for each winner to enumerate paths
    for path_num, board in enumerate(all_winners):
        find_path(board, path_num)

    print_winners(all_boards, num_strategies)

if __name__ == '__main__':
    main()
