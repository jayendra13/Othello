import numpy as np

class Othello(object):
    """docstring for Othello."""
    def __init__(self):
        super(Othello, self).__init__()
        self.board = np.ones((8,8), dtype=np.int8)*-1

    def init_board(self):
        self.board[3][3] = 1
        self.board[4][4] = 1
        self.board[3][4] = 0
        self.board[4][4] = 0

    def _get_neighbours(self, x):
        n = np.array([x-9, x-8,x-7,x-1,x+1,x+7,x+8,x+9])
        n = n[np.logical_and(n>=0,n<=63)]
        return n
