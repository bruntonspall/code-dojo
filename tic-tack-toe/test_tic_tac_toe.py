"""
Nosetests for tic-tac-toe.py

see http://somethingaboutorange.com/mrl/projects/nose/
"""
from tic_tac_toe import game, NAUGHT, CROSS, EMPTY

def full_integration_test():
    """ 
    A first test to get things rolling...

    PLEASE CHANGE ANYTHING SHOULD YOU DISAGREE WITH THE ASSUMPTIONS MADE HERE

    This test makes sure there is a function (that you might want to rename) 
    that will appropriately update the game state given the following (that you
    might also want to change - hell, anything is up for grabs here):

    # The state of the board is a list containing nine items. 

    # Each item can be in one of the following states:

        1) "X" = represents a cross
        2) "O" = represents a naught
        3) "_" = represents an empty space

    # Each position in the array maps to the board in the following way:

        0 | 1 | 2
        ---------
        3 | 4 | 5
        ---------
        6 | 7 | 8

    # To place a piece on the board call the function with the position number 
    and type of piece.

    # The function will return a status message and the array representing the
    current state of the game. 

    # The status messages will be one of the following:
        "OK" - you successfully place the piece on a location represented by "_"
        "TAKEN" - you attempted to place a piece on a location already taken
        "BAD TURN" - you attempt to place a piece out of turn
        "FOO WINS" - where FOO is either X or O when they've won the game
    """
    #ttt = game()
    #status, state = ttt.play()
    #assert state == [ EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, ]
    #assert status == 'OK'
    #status, state = ttt.play(CROSS, 0)
    #assert state == [ CROSS, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, ]
    #assert status == 'OK'
    #status, state = ttt.play(NAUGHT, 5)
    #assert state == [ CROSS, EMPTY, EMPTY, EMPTY, EMPTY, NAUGHT, EMPTY, EMPTY, EMPTY, ]
    #assert status == 'OK'
    #status, state = ttt.play(CROSS, 0)
    #assert state == [ CROSS, EMPTY, EMPTY, EMPTY, EMPTY, NAUGHT, EMPTY, EMPTY, EMPTY, ]
    #assert status == 'TAKEN'
    #status, state = ttt.play(NAUGHT, 6)
    #assert state == [ CROSS, EMPTY, EMPTY, EMPTY, EMPTY, NAUGHT, EMPTY, EMPTY, EMPTY, ]
    #assert status == 'BAD TURN'
    #status, state = ttt.play(CROSS, 1)
    #assert state == [ CROSS, CROSS, EMPTY, EMPTY, EMPTY, NAUGHT, EMPTY, EMPTY, EMPTY, ]
    #assert status == 'OK'
    #status, state = ttt.play(NAUGHT, 6)
    #assert state == [ CROSS, CROSS, EMPTY, EMPTY, EMPTY, NAUGHT, NAUGHT, EMPTY, EMPTY, ]
    #assert status == 'OK'
    #status, state = ttt.play(CROSS, 2)
    #assert state == [ CROSS, CROSS, CROSS, EMPTY, EMPTY, NAUGHT, NAUGHT, EMPTY, EMPTY, ]
    #assert status == 'X WINS'

def test_we_can_setup_board():
    """ This is a basic test to ensure that we can setup a valid board"""

    ttt = game()
    assert ttt.board == [ EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, ]

def test_can_place_counter_on_board():
    """ Test that we can place tokens on the board """

    ttt = game()
    ttt.play(CROSS, 0)
    assert ttt.board == [ CROSS, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, ]
    ttt.play(NAUGHT, 1)
    assert ttt.board == [ CROSS, NAUGHT, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, ]

def test_cannot_place_token_on_existing_token():
    """ Test that we cannot place a token over hte top of an existing token """

    ttt = game()
    ttt.play(CROSS, 0)
    assert ttt.board == [ CROSS, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, ]
    status = ttt.play(NAUGHT, 0)
    assert ttt.board == [ CROSS, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, ]
    assert status == 'TAKEN'

def test_that_x_must_go_first():
    """ Test that we cannot place tokens out of turn.
            Player X goes first
    """

    ttt = game()
    status = ttt.play(NAUGHT, 0)
    assert ttt.board == [ EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, ]
    assert status == 'BAD TURN'

def test_that_x_must_go_first():
    """ Test that we cannot place tokens out of turn.
            Each player takes alternating turns
    """

    ttt = game()
    status = ttt.play(CROSS, 0)
    status = ttt.play(CROSS, 1)
    assert ttt.board == [ CROSS, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, ]
    assert status == 'BAD TURN'

    # Advance a turn
    status = ttt.play(NAUGHT, 1)

    status = ttt.play(NAUGHT, 2)
    assert ttt.board == [ CROSS, NAUGHT, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, ]
    assert status == 'BAD TURN'

def test_for_winning_line():
    """ Test that we can win by placing a horizontal line. """

    ttt = game()
    ttt.board = [ CROSS, CROSS, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, NAUGHT, NAUGHT, ]

    status = ttt.play(CROSS, 2)
    assert ttt.board == [ CROSS, CROSS, CROSS, EMPTY, EMPTY, EMPTY, EMPTY, NAUGHT, NAUGHT, ]
    assert status == 'CROSS WINS'

def test_for_all_winning_horizontal_lines():
    """ Test that we can win by placing a horizontal line. """

    ttt = game()
    ttt.board = [ CROSS, CROSS, CROSS, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, ]
    assert ttt._validate_win()

    ttt.board = [ EMPTY, EMPTY, EMPTY, CROSS, CROSS, CROSS, EMPTY, EMPTY, EMPTY, ]
    assert ttt._validate_win()

    ttt.board = [ EMPTY, EMPTY, EMPTY, EMPTY, NAUGHT, NAUGHT, CROSS, CROSS, CROSS, ]
    assert ttt._validate_win()

