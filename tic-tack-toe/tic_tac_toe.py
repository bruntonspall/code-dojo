class game:
    """
    A stub to change
    """
    EMPTY = '_'
    CROSS = 'X'
    NAUGHT = 'O'

    def __init__(self):
        self.board = [game.EMPTY, game.EMPTY, game.EMPTY, game.EMPTY, game.EMPTY, game.EMPTY, game.EMPTY, game.EMPTY, game.EMPTY]
        self.play_next = self.CROSS

    def _toggle_turn(self):
        if self.play_next == self.CROSS:
            self.play_next = self.NAUGHT
        else:
            self.play_next = self.CROSS

    def play(self, token=None, pos=None):
        """
        Places a token if possible
        """
        if token != self.play_next:
            return 'BAD TURN'
        if self.board[pos] != self.EMPTY:
            return 'TAKEN'
        else:
            self.board[pos] = token
            self._toggle_turn()
