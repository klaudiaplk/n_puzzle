from pszt_n_puzzle.board import Board
from pszt_n_puzzle.state import State
from pszt_n_puzzle.state_search import State_search

    
    
#input = [[13, 2, 10, 3], [1, 12, 8, 4], [5, -1, 9, 6], [15, 14, 11, 7]]
#input = [[7, 2, 4], [5, -1, 6], [8, 3, 1]]
input = [[1, 2, 3], [7, 4, 6], [5, -1, 8]]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, -1]]
#goal = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, -1]]
n = 3
#input = generate_board(8)
board = Board(n, input)
state = State(board, goal, "BFS", 0)
state.setHeuristicValue()
board.printBoard()
if state.isSolvable():
    #print('tutaj')
    state_search = State_search(state)
    path = state_search.search_A_star()
    #print(path)
    #print('tutaj2')
    for i in reversed(path):
        i.getBoard().printBoard()
    print('Checked states', state_search.getCheckedCount())
    print("Used process time: {:.4f}s".format(state_search.getUsedTime()))
else:
    exit(1)
