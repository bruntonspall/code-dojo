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
