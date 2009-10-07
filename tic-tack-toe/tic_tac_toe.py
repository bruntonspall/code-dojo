class game:
    """
    A stub to change
    """
    EMPTY = '_'

    def __init__(self):
        self.board = [game.EMPTY, game.EMPTY, game.EMPTY, game.EMPTY, game.EMPTY, game.EMPTY, game.EMPTY, game.EMPTY, game.EMPTY]

    def play(self, token=None, pos=None):
        """
        Places a token if possible
        """
        if token == 'O':
            return 'BAD TURN'
        if self.board[pos] == self.EMPTY:
            self.board[pos] = token
        else:
            return 'TAKEN'
