class game:
    """
    A stub to change
    """
    EMPTY = '_'

    def __init__(self):
        self.board = [game.EMPTY, game.EMPTY, game.EMPTY, game.EMPTY, game.EMPTY, game.EMPTY, game.EMPTY, game.EMPTY, game.EMPTY]

    def play(self, token=None, pos=None):
        """
        Please finish
        """
        self.board[pos] = token
