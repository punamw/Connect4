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





def main():
    """
    Play ze game :)
    """
    turn = "player"
    print("Welcome to Connect 4 /n Human plays as X, Computer as O")
    Board.drawBoard()
    
