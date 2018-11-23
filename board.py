

class Board:

    def __init__(self):
        self.board = None
        self.isEmpty = None
        self.tile = None
        self.height = 4
        self.width = 5

    def createBoard(self):
        """
        Board to look like this:

        01 | 02 | 03 | 04 | 05 |
        06 | 07 | 08 | 09 | 10 |
        11 | 12 | 13 | 14 | 15 |
        16 | 17 | 18 | 19 | 20 |

        :)
        """

        self.board = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
                 "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]




    def getBoard(self):
        return self.board

    def drawBoard(self):
        """
        Draw the board lol
        :return:
        """
        line = "|"
        count=0
        for i in self.board:
            count+=1
            display = i + "|"
            line += display
            if count % 5 == 0:
                print(line)
                line = "|"
        print("\n")


    def updateBoard(self, player, position):
        """
        Take in player move and update board. Assume move is valid and in correct spot.
        :param player: human or computer (string)
        :param position: index value where player wants to move
        :return:
        """

        if player == "human":
            char = "X"
        else:
            player = "computer"
            char = "O"

        self.board[int(position)] = char
        print(player + " move")
        self.drawBoard()
