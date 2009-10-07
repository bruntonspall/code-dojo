class game:
    """
    A stub to change
    """
    EMPTY = '_'

    def __init__(self):
        self.board = [game.EMPTY, game.EMPTY, game.EMPTY, game.EMPTY, game.EMPTY, game.EMPTY, game.EMPTY, game.EMPTY, game.EMPTY]
        self.play_next = 'X'

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
            if self.play_next == 'X':
                self.play_next = 'O'
            else:
                self.play_next = 'X'
