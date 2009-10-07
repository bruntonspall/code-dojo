"""
Nosetests for tic-tac-toe.py

see http://somethingaboutorange.com/mrl/projects/nose/
"""
import tic_tac_toe

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
    #ttt = tic_tac_toe.game()
    #status, state = ttt.play()
    #assert state == [ '_', '_', '_', '_', '_', '_', '_', '_', '_', ]
    #assert status == 'OK'
    #status, state = ttt.play('X', 0)
    #assert state == [ 'X', '_', '_', '_', '_', '_', '_', '_', '_', ]
    #assert status == 'OK'
    #status, state = ttt.play('O', 5)
    #assert state == [ 'X', '_', '_', '_', '_', 'O', '_', '_', '_', ]
    #assert status == 'OK'
    #status, state = ttt.play('X', 0)
    #assert state == [ 'X', '_', '_', '_', '_', 'O', '_', '_', '_', ]
    #assert status == 'TAKEN'
    #status, state = ttt.play('O', 6)
    #assert state == [ 'X', '_', '_', '_', '_', 'O', '_', '_', '_', ]
    #assert status == 'BAD TURN'
    #status, state = ttt.play('X', 1)
    #assert state == [ 'X', 'X', '_', '_', '_', 'O', '_', '_', '_', ]
    #assert status == 'OK'
    #status, state = ttt.play('O', 6)
    #assert state == [ 'X', 'X', '_', '_', '_', 'O', 'O', '_', '_', ]
    #assert status == 'OK'
    #status, state = ttt.play('X', 2)
    #assert state == [ 'X', 'X', 'X', '_', '_', 'O', 'O', '_', '_', ]
    #assert status == 'X WINS'

def test_we_can_setup_board():
    """ This is a basic test to ensure that we can setup a valid board"""

    ttt = tic_tac_toe.game()
    assert ttt.board == [ '_', '_', '_', '_', '_', '_', '_', '_', '_', ]

def test_can_place_counter_on_board():
    """ Test that we can place tokens on the board """

    ttt = tic_tac_toe.game()
    ttt.play('X', 0)
    assert ttt.board == [ 'X', '_', '_', '_', '_', '_', '_', '_', '_', ]
    ttt.play('X', 1)
    assert ttt.board == [ 'X', 'X', '_', '_', '_', '_', '_', '_', '_', ]

def test_cannot_place_token_on_existing_token():
    """ Test that we cannot place a token over hte top of an existing token """

    ttt = tic_tac_toe.game()
    ttt.play('X', 0)
    assert ttt.board == [ 'X', '_', '_', '_', '_', '_', '_', '_', '_', ]
    status = ttt.play('O', 0)
    assert ttt.board == [ 'X', '_', '_', '_', '_', '_', '_', '_', '_', ]
    assert status == 'TAKEN'
