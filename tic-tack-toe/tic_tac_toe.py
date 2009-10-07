EMPTY = '_'
CROSS = 'X'
NAUGHT = 'O'

class game:
    """
    A stub to change
    """

    def __init__(self):
        self.board = [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]
        self.play_next = CROSS

    def _toggle_turn(self):
        if self.play_next == CROSS:
            self.play_next = NAUGHT
        else:
            self.play_next = CROSS

    def play(self, token=None, pos=None):
        """
        Places a token if possible
        """
        if token != self.play_next:
            return 'BAD TURN'
        if self.board[pos] != EMPTY:
            return 'TAKEN'
        else:
            self.board[pos] = token
            self._toggle_turn()

        if self.board[0] == self.board[1] and self.board[1] == self.board[2]:
            return 'CROSS WINS'
        if self.board[3] == self.board[4] and self.board[4] == self.board[5]:
            return 'CROSS WINS'
        if self.board[6] == self.board[7] and self.board[7] == self.board[8]:
            return 'CROSS WINS'
