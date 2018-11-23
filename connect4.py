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

    runCheck = True

    while runCheck:
        pmove = input("Enter a move: ")
        if pmove.upper() == "H":
            displayInstructions()
            b.drawBoard()
        else:
            pvalid = m.isValid(pmove, board)
            # if true - valid move
            if pvalid:
                pmove = m.makePlayerMove(pmove, board)
                b.updateBoard(turn, pmove)
                # stop loop for checking move
                runCheck = False
    return

def displayInstructions():
    goals = """
    GOAL
    The point of the game is get 4 of your tiles (X) in a row either diagonally, horizontally, or vertically. 
    
    MOVEMENT
    Players can move by selecting a number on the board. No matter which available number on the board is chosen,
    the tile will "drop" to the bottom or to the next available spot. A spot is available if neither player has
    made a move on that specific spot (i.e not X nor O). Only moves made between 1-20 are valid - the player will
     be forced to select another move if it is not within 1-20.
    
    WINNING
    The game ends once either player gets 4 tiles in a row.
            """
    print(goals)


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
    print("To view instructions, input 'H'.")
    b.createBoard() #create the board to play
    b.drawBoard() #draw the board

    playerMove()


main()
