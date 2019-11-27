import copy


class Board:

    def __init__(self, n, board):
        self.n = n
        self.board = board

    def getBlankPosition(self):
        x = 0
        y = 0
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board)):
                if self.board[i][j] == -1:
                    x = j
                    y = i
        return [x, y]

    def getNeighbors(self):
        neighbors_boards = []
        x, y = self.getBlankPosition()
        shifts = [[x, y + 1], [x, y - 1], [x + 1, y], [x - 1, y]]
        for shift in shifts:
            if shift[0] >= 0 and shift[0] < len(self.board) and shift[1] >= 0 and shift[1] < len(self.board):
                new_board = copy.deepcopy(self.board)
                current_board = Board(self.n, new_board)
                current_board.moveBlank(shift)
                neighbors_boards.append(current_board)

        return neighbors_boards

    def moveBlank(self, shift):
        blank_x, blank_y = self.getBlankPosition()
        x, y = shift
        tmp = self.board[y][x]
        self.board[y][x] = -1
        self.board[blank_y][blank_x] = tmp


    def printBoard(self):
        print('print')
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board)):
                print("{:2d}".format(self.board[i][j]), end = ' ')
            print()
        print('--------------')


    def getBoard(self):
        return self.board

    def __str__(self):
        string = ""
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board)):
                string += "{:2d}".format(self.board[i][j]) + " "
            string += "\n"
        string += '--------------'
        string += "\n"
        return string
