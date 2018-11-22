

class Board():

    def __init__():
        self.board = None
        self.isEmpty = None
        self.tile = None
        self.height = 4
        self.width = 5

    def createBoard():

        legend = [ "|", "1","|", "1", "|", "3", "|", "4", "|", "5", "|" ]
        row = [ "|", "","|", "", "|", "", "|", "", "|", "", "|" ]
        sep = ["-","-","-","-","-"]

        board = legend + sep + row + sep + row + sep +row + sep +row + sep +row + sep
        return board
