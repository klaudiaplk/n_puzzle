class State:

    def __init__(self, board, goal, heuristic_type, depth):
        """Init.

        :param board: input board
        :param goal: output board
        :param heuristic_type: name of the heuristic we want to use
        :param depth: depth we are currently in
        """
        self.board = board.getBoard()
        self.obj_board = board
        self.goal = goal
        self.heuristic_type = heuristic_type
        self.depth = depth
        self.val_heuristic = 0
        self.parent = None

    def setHeuristicValue(self):
        """Set heuristic value.

        """
        if self.heuristic_type == "manhattan":
            self.val_heuristic = self.getManhattan() + self.depth
        elif self.heuristic_type == "misplaced_tiles":
            self.val_heuristic = self.getMisplacesTiles() + self.depth
        elif self.heuristic_type == "BFS":
            self.val_heuristic = self.depth

    def getMisplacesTiles(self):
        """Get value of misplaces tiles heuristic.

        :return: value of misplaces tiles heuristic
        """
        misplaces_tiles = 0
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board)):
                if self.board[i][j] != self.goal[i][j] and self.board[i][j] != -1:
                    misplaces_tiles += 1
        return misplaces_tiles

    def getManhattan(self):
        """Get value of manhattan heuristic.

        :return: value of manhattan heuristic
        """
        elem = {}
        sum = 0
        for i in range(0, len(self.goal)):
            for j in range(0, len(self.goal)):
                elem[self.goal[i][j]]=[j, i]
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board)):
                if(self.board[i][j] != -1):
                    x1, y1 = elem[self.board[i][j]]
                    sum += abs(i-y1) + abs(j-x1)
        return sum

    def getNeighbors(self):
        """Get Neighbors for blank space.

        :return: list of neighbors
        """
        neighbors_list = []
        neighbors = self.obj_board.getNeighbors()
        for neighbor in neighbors:
            cur_state = State(neighbor, self.goal, self.heuristic_type, self.depth + 1)
            if cur_state.isSolvable():
                cur_state.setHeuristicValue()
                cur_state.setParent(self)
                neighbors_list.append(cur_state)
        return neighbors_list

    def isSolvable(self):
        """Function responsible for checking if a solution exists for a given board.

        :return: value saying whether a solution is possible for the board
        """
        solvable = False
        inversion_count = self.countInversion()
        if len(self.board) % 2 != 0:
            if inversion_count % 2 == 0:
                solvable = True
        else:
            x, y = self.obj_board.getBlankPosition()
            # even row counting from bottom
            if y % 2 == 0:
                if inversion_count % 2 != 0:
                    solvable = True
            else:
                if inversion_count % 2 == 0:
                    solvable = True
        return solvable

    def countInversion(self):
        """Count Manhattan heuristic.

        :return: number of times the larger number is after the smaller number
        """
        inversion_list = []
        for i in range(0, len(self.board)):
            inversion_list.extend(self.board[i])
        sum = 0
        for i in range(0, len(inversion_list) - 1):
            current = inversion_list[i]
            for j in range(i + 1, len(inversion_list)):
                if inversion_list[j] < current and inversion_list[j] != -1:
                    sum += 1

        return sum

    def isSolution(self):
        return self.getMisplacesTiles() == 0

    def getParent(self):
        return self.parent

    def getHeuristic(self):
        return self.val_heuristic

    def setParent(self, parent):
        self.parent = parent

    def setHeuristic(self, val_heuristic):
        self.val_heuristic = val_heuristic

    def getBoard(self):
        return self.obj_board

    def getDepth(self):
        return self.depth

    def __hash__(self):
        return hash(tuple([tuple(i) for i in self.board]))

    def __eq__(self, other):
        return self.board == other.board

    def __lt__(self, other):
        if self.val_heuristic == other.getHeuristic():
            return self.depth < other.getDepth()
        else: 
            return self.val_heuristic < other.getHeuristic()

    def __str__(self):
        string = ""
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board)):
                string += str(self.board[i][j]) + " "
            string += "\n"
            string += "heurystyka "
            string += str(self.val_heuristic)
            string += "\n"
        return string

