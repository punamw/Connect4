## MAIN PROGRAM

from move import Move
from board import Board
from win import Win


def checkGameWin():
    """
    Check if move played resulted in a win. Return false if keep playing and no win condition.
    :return: boolean true or false
    """

    global turn#, play
    board = b.getBoard()
    isWin = w.checkAll(turn, board)
    if isWin == True:
        #play = False
        if turn == "human":
            print("YOU WON!!")
        else:
            print("YOU LOSE :(")
        return False
    else:
        return True

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
        print("\n")
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

    #check if it can make a winning move --else play random move
    cmove = m.check_winning_move(board)
    if cmove != False:
        b.updateBoard("computer", cmove)
    else:
        cmove = m.makeComputerMove(board)
        b.updateBoard("computer", cmove)
    return


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
    global turn, b, m, w, play
    b = Board()
    m = Move()
    w = Win()
    #play = True
    print("Welcome to Connect 4. Human plays as X, Computer as O.")
    print("To view instructions, input 'H'.")

    b.createBoard() #create the board to play
    b.drawBoard() #draw the board

    while True:
        # human turn
        turn = "human"
        playerMove()
        keep_playing = checkGameWin() # FIXME - variable play will not affect this loop since it is a copy
        if keep_playing is False:
            return False
        # computer turn
        turn = "computer"
        computerMove()
        checkGameWin()
        if keep_playing is False:
            return False

    #TODO:return the winner


    # TODO - make win conditions




main()
