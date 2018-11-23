## MAIN PROGRAM

"""
OUTLINE
1. Draw board + create it
2. Player move
3. Computer move
4. Repeat moves until someone ones (4 connected)
"""

from move import Move
from board import Board

def playerMove():
    global turn
    board = b.getBoard()
    isValid = True
    while isValid:
        pmove = input("Enter number of move to make: ")
        pvalid = m.isValid(pmove, board)
        if pmove:
            b.updateBoard(turn, pmove)
            isValid = False
    return




def main():
    """
    Play ze game :)
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
