# creating a sodoku solver

class Board:
    # the __init__ method is like a constructor
    def __init__(self, board):
        self.board = board

    def solveBoard(self):
        # we need to loop through every field of the board
        testingNumber = 1
        row = 0
        while row < len(self.board):
            field = 0
            while field < len(self.board[row]):
                # first check if the field is empty
                if(self.board[row][field] == 0):
                    # check if the whole row contains the same number as "testingNumber"
                    for checkRow in self.board[row]:
                        print(checkRow)
                        if(checkRow == testingNumber):
                            break
                field += 1
            row += 1
            testingNumber += 1
                
                    



# the board is a two dimensional array
board1 = Board([[0, 0, 4, 8, 6, 0, 0, 3, 0], [0, 0, 1, 0, 0, 0, 0, 9, 0], [8, 0, 0, 0, 0, 9, 0, 6, 0], [5, 0, 0, 2, 0, 6, 0, 0, 1], [
               0, 2, 7, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 4, 3, 0, 0, 6], [0, 5, 0, 0, 0, 0, 0, 0, 0], [0, 0, 9, 0, 0, 0, 4, 0, 0], [0, 0, 0, 4, 0, 0, 0, 1, 5]])

board1.solveBoard()