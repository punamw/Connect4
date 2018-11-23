import random
"""
# column wins
[(0,5,10,15), (1,6,11,16), (2,7,12,17), (3,8,13,18),(4,9,14,19)]

# rows
[(0,1,2,3), (1,2,3,4) (5,6,7,8), (6,7,8,9), (10,11,12,13), (11,12,13,14), (15,16,17,18), (16,17,18,19)]

# diagonals
[(0,6,12,18), (1,7,13,19), (15,11,7,3), (16,12,8,4), (19,13,8,2), (18,12,6,0)]

Board to look like this:

01 | 02 | 03 | 04 | 05 |
06 | 07 | 08 | 09 | 10 |
11 | 12 | 13 | 14 | 15 |
16 | 17 | 18 | 19 | 20 |

:)
"""


class Move:

    def __init__(self):
        self.columnWins = [{0,5,10,15}, {1,6,11,16}, {2,7,12,17}, {3,8,13,18},{4,9,14,19}]
        self.rowWins = [{0, 1, 2, 3}, {1, 2, 3, 4},{5, 6, 7, 8},{6, 7, 8, 9}, {10, 11, 12, 13}, {11, 12, 13, 14},{15, 16, 17, 18}, {16, 17, 18, 19}]
        self.diagonalWins = [{0,6,12,18},{1,7,13,19}, {15,11,7,3}, {16,12,8,4}, {19,13,8,2}, {18,12,6,0}]


    def check_winning_move(self, board):
        """
        Find ze winning move lel
        Computer is O
        :return: will return winning move if exists or None --> returns winning move index!!
        """
        #retrieve current computer moves played
        currentMoves = self.getCPMoves()

        #check column win
        is_col_win = self.checkColumn(currentMoves, self.columnWins)
        if is_col_win != False:
            return is_col_win

        #check row win
        is_row_win = self.checkRow(currentMoves, self.rowWins)
        if is_row_win != False:
            return is_row_win

    def makeMove(self, board):
        #makes a random move
        valid = False
        while valid:
            moves = self.getAvalMoves(board)
            move = random.sample(moves)
            validMove = self.isValid(move, board)
            if validMove:
                valid = True
        return validMove

    def isValid(self, move, board):
        avalMoves = self.getAvalMoves(board)
        move = int(move)+5
        if str(move) in avalMoves:
            return False
        else:
            return True

    def getCPMoves(self, board):
        #first find all positions that the computer holds
        #currentMoves holds the indices where the computer has made a move
        currentMoves = []
        i=-1
        for char in board:
            i +=1
            if char == "O":
                currentMoves.append(i)
        return currentMoves

    def getAvalMoves(self, board):
        #get available moves, returns an array of indexes with available moves
        i=-1
        avalMoves= []
        for char in board:
            i+=1
            if char !="X" or char !="O":
                avalMoves.append(i)
        return avalMoves



    def checkColumn(self, cpMoves, columnWins, board):
        #check for column wins
        for seq in columnWins:
            checkThree = True
            for i in seq[1:]:
                if i not in cpMoves:
                    checkThree = False
                    break
            if checkThree and board[i-5]!="X":
                return i-5
        return False




    def checkRow(self,cpMoves, rowWins, board):
        #check for row wins
        for seq in rowWins:
            count = 0
            for i in seq:
                if i in cpMoves:
                    count +=1
                else:
                    notIn = i
            if count ==3 and board[notIn]!="X":
                return notIn
        return False

    def checkDiagonal(self, cpMoves, diagonalWins, board):
        #check for diagonal wins
        for seq in diagonalWins:
            checkThree = True
            for i in seq[1:]:
                if i not in cpMoves:
                    checkThree = False
                    break
            if checkThree and board[i-6]!="X":
                return i-6
        return False
