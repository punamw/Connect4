"--------------------CHECK FOR WINS-------------------"


class Win:

    def __init__(self):
        self.columnWins = [{0,5,10,15}, {1,6,11,16}, {2,7,12,17}, {3,8,13,18},{4,9,14,19}]
        self.rowWins = [{0, 1, 2, 3}, {1, 2, 3, 4},{5, 6, 7, 8},{6, 7, 8, 9}, {10, 11, 12, 13}, {11, 12, 13, 14},{15, 16, 17, 18}, {16, 17, 18, 19}]
        self.diagonalWins = [{0,6,12,18},{1,7,13,19}, {15,11,7,3}, {16,12,8,4}, {19,13,8,2}, {18,12,6,0}]

    def checkAll(self, player, board):

        """
        See if move just made results in a win
        :return: True if win else False
        """
        #retrieve current moves of the player who made the last move
        currentMoves = self.getPlayerMoves(player,board)

        #check column win
        is_col_win = self.checkWin(currentMoves, self.columnWins)
        if is_col_win != False:
            return True

        #check row win
        is_row_win = self.checkWin(currentMoves, self.rowWins)
        if is_row_win != False:
            return True

        #check diagonal win
        is_diag_win = self.checkWin(currentMoves, self.diagonalWins)
        if is_diag_win != False:
            return True
        else:
            return False

    #return an array of indexes in which the player has made a move
    def getPlayerMoves(self, player, board):

        currentMoves = []
        i=-1
        if player == "human":
            for char in board:
                i +=1
                if char == "X":
                    currentMoves.append(i)
        else:
            for char in board:
                i +=1
                if char == "O":
                    currentMoves.append(i)
        return currentMoves

    def checkWin(self, moves, section):
        for seq in section:
            count = 0
            for i in seq:
                if i in moves:
                    count +=1
            if count ==4:
                return True
        return False
