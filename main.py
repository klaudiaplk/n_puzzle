from board import Board
from state import State
from state_search import State_search

def main():
    
    input = [[1, 2, 3], [-1, 4, 6], [7, 5, 8]]
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, -1]]
    n = 3
    
    board = Board(n, input)
    state = State(board, goal, "Misplaces tiles", 0)
    state.setHeuristicValue()
    
    if state.isSolvable():
       
        state_search = State_search(state)
        path = state_search.search_A_star()
        #print(path)
        for i in reversed(path):
            i.getBoard().printBoard()
    else:
        exit(1)

main()
