---
title: 'Solitaire Chess in Python.'
layout: default
---

Here is an example of Breadth First Search (BFS) to traverse a graph and find all possible paths. The graph here is a representation of a 4x4 chess board in the game of [solitaire chess](http://www.thinkfun.com/microsite/solitairechess/demo). The pieces are standard chess pieces. The only legal moves are captures of other pieces. Pawns only being able to move downward.  
The board starts in a random configuration, and the objective of the puzzle is to be left with only one piece.  
An interesting programming problem related to this game: Create a program that can accept an arbitrary board state as input and determine if there is a solution. If there are solutions, print out all steps for each one.  
The steps to programming this solution are as follows:
1. Create classes for each type of piece, with methods for the available move directions that test for boundaries
2. Create a class for the board state with the methods to find all available moves from the current state. Include an attribute for marking the parent of the board state- that is, which board came before the current one, with `None` as the parent of the starting board.
3. For the BFS, create a queue (from `collections.deque`) to store the board states for testing each one. As new board states are found from each one tested, push them on to the back of the queue.

The actual BFS algorithm looks like this, where `Board_state.size()` is a method to list how many pieces are left on the board, and `Board_state.win_paths` is list of the indices to keep track of which winning paths the state was a part of.

    def run_BFS(start_board, queue):
        all_boards = []
        win_idx = 0

        queue.append(start_board)

        while len(queue) > 0:
            cur = queue.popleft()
            all_boards.append(cur)

            if cur.size() > 1:
                new_boards = cur.find_all_captures()
                queue.extend(new_boards)
            else:
                cur.win_paths.append(win_idx)
                win_idx += 1

        num_strategies = win_idx

        return all_boards, num_strategies


If we were to use Depth First Search (DFS), the algorithm would look like this:

    def run_DFS(start_board, stack):
        stack.append(start_board)

        all_boards = []
        win_idx = 0

        while len(stack) > 0:
            cur = stack.pop()
            all_boards.append(cur)

            if cur.size() > 1:
                new_boards = cur.find_all_captures()
                stack.extend(new_boards)
            else:
                cur.win_paths.append(win_idx)
                win_idx += 1

        num_strategies = win_idx

        return all_boards, num_strategies


The main difference here is that we are using stack instead of a queue, though in python they can be the same data structure- a deque. The deque and a normal `list` would be the same here, as we are simply popping graph nodes on top of the stack and removing one at each iteration.  
The difference in DFS is that the nodes that were most recently placed on top are examined first, leading to some solution along a path quicker. If we were to stop at the first possible solution, DFS would be usually be quicker (unless the one solution were the last branch of the graph).
