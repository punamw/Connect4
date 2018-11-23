## MAIN PROGRAM

from move import Move
from board import Board

def playerMove():
    """
    Allows the player to make a move
    :return: None
    """
    global turn
    board = b.getBoard()

    # TODO - maybe change variable name?
    runCheck = True

    while runCheck:
        pmove = input("Enter number of moves to make: ")
        pvalid = m.isValid(pmove, board)
        # if true - valid move
        if pvalid:
            pmove = m.makePlayerMove(pmove, board)
            b.updateBoard(turn, pmove)
            # stop loop for checking move
            runCheck = False
    return


def main():
    """
    OUTLINE
    1. Draw board + create it
    2. Player move
    3. Computer move
    4. Repeat moves until someone ones (4 connected)
    """
    global turn, b, m
    b = Board()
    m = Move()
    turn = "human"
    print("Welcome to Connect 4. Human plays as X, Computer as O.")
    b.createBoard() #create the board to play
    b.drawBoard() #draw the board

    playerMove()


main()
