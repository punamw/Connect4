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
        currentMoves = self.getCPMoves(board)

        #check column win
        is_col_win = self.checkColumn(currentMoves, self.columnWins, board)
        if is_col_win != False:
            return is_col_win

        #check row win
        is_row_win = self.checkRow(currentMoves, self.rowWins, board)
        if is_row_win != False:
            return is_row_win

        #check diagonal win
        is_diag_win = self.checkRow(currentMoves, self.diagonalWins, board)
        if is_diag_win != False:
            return is_diag_win

        else:
            return False

    def makeComputerMove(self, board):
        """
        Allows the computer to make a move. Moves are chosen randomly.
        :param board: array representation of board
        :return: index position of computer's move
        """
        #makes a random move
        valid = False
        while not valid:
            moves = self.getAvalMoves(board)
            move = random.sample(moves,1) # assume index selection
            move = move[0]
            validMove = self.isValid(move, board)
            # make the move by dropping it
            if validMove:
                #valid = True

                if move + 15 in moves:
                    move += 15
                    # 3rd row
                elif move + 10 in moves:
                    move += 10
                    # 2nd row
                elif move + 5 in moves:
                    move += 5
                    # 1st row
                elif move in moves:
                    pass
                return move

    def makePlayerMove(self, move,board):
        """
        Sets the move for the player - with gravity. Assume valid move.
        :return: None
        """

        # make into integer and set to proper index value
        move = int(move)
        move -= 1

        avalMoves = self.getAvalMoves(board)

        # 4th row
        if move + 15 in avalMoves:
            move += 15
        # 3rd row
        elif move + 10 in avalMoves:
            move += 10
        # 2nd row
        elif move + 5 in avalMoves:
            move += 5
        # 1st row
        elif move in avalMoves:
            pass

        return move


    def isValid(self, move, board):
        """
        Check if current move is legal
        :param move: move chosen
        :param board: array board currently used
        :return: boolean true or false
        """
        # check if a number - return false if string
        try:
            move = int(move)
        except Exception:
            return False

        avalMoves = self.getAvalMoves(board)

        # correct input to proper index found in board array
        # ex. if input = 20, index should be 19
        move -= 1

        ## Check if valid move
        # Inputted value not within board
        if move < 0 or move > 19:
            return False
        # 4th row
        elif move + 15 in avalMoves:
            pass
        # 3rd row
        elif move + 10 in avalMoves:
            pass
        # 2nd row
        elif move + 5 in avalMoves:
            pass
        # 1st row
        elif move in avalMoves:
            pass
        # column is full
        else:
            return False

        return True

        # #move = int(move)+5
        # print(move)
        #
        # # check if available move
        # if str(move) in avalMoves:
        #     print(False)
        #     return False
        # else:
        #     print(True)
        #     return True

    def getCPMoves(self, board):
        """
        Finds all the positions that the computer (O) currently holds.
        :param board: current board
        :return: array of index positions that the computer holds
        """
        # currentMoves holds the indices where the computer has made a move
        currentMoves = []
        i=-1
        for char in board:
            i +=1
            if char == "O":
                currentMoves.append(i)
        return currentMoves

    def getAvalMoves(self, board):
        """
        Find array of all possible moves the player can make
        :param board: array board to be used
        :return: array of possible move indexes
        """

        #i = -1 # value in board
        avalMoves= []
        for char in board:
            #i+=1
            if char !="X" and char !="O":
                avalMoves.append(board.index(char))
        return avalMoves



    def checkColumn(self, cpMoves, columnWins, board):
        """
        Check for column wins
        :param cpMoves: computer move (index)
        :param columnWins: array of sets containing winning column positions
        :param board: current board
        :return: boolean false or index position
        """

        for seq in columnWins:
            count = 0
            for i in seq:
                if i in cpMoves:
                    count +=1
                else:
                    notIn = i
            if count ==3 and board[notIn]!="X":
                return notIn
        return False




    def checkRow(self,cpMoves, rowWins, board):
        """
        Check for row wins
        :param cpMoves: computer move index
        :param rowWins: array of sets for row wins indexes
        :param board: current board
        :return: false or index position
        """
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
        """
        Check for diagonal wins
        :param cpMoves: computer move index
        :param rowWins: array of sets for row wins indexes
        :param board: current board
        :return: false or index position
        """
        for seq in diagonalWins:
            checkThree = True
            for i in seq[1:]:
                if i not in cpMoves:
                    checkThree = False
                    break
            if checkThree and board[i-6]!="X":
                return i-6
        return False
