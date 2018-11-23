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

    # check input and keep running until actual move is made
    while runCheck:
        pmove = input("Enter a move: ")
        # instructions
        if pmove.upper() == "H":
            displayInstructions()
            b.drawBoard()
        # else just an attempted move
        else:
            pvalid = m.isValid(pmove, board)
            # if true - valid move
            if pvalid:
                pmove = m.makePlayerMove(pmove, board)
                b.updateBoard(turn, pmove)
                # stop loop for checking move
                runCheck = False
    return

def computerMove():
    """
    Let the computer make a move.
    :return: None
    """
    board = b.getBoard()

    cmove = m.makeComputerMove(board)
    b.updateBoard("computer", cmove)

def displayInstructions():
    """
    Display game instructions.
    :return: None
    """
    instructions = """
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
    print(instructions)


def main():
    """
    OUTLINE
    1. Draw board + create it
    2. Player move
    3. Computer move
    4. Repeat moves until someone one wins (4 connected)
    """
    global turn, b, m
    b = Board()
    m = Move()
    print("Welcome to Connect 4. Human plays as X, Computer as O.")
    print("To view instructions, input 'H'.")

    # TODO - make loop until win
    # TODO - make win conditions

    # human turn
    turn = "human"
    b.createBoard() #create the board to play
    b.drawBoard() #draw the board
    playerMove()

    # computer turn
    turn = "computer"
    computerMove()


main()
