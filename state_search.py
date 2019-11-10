from state import State
from collections import deque
import heapq
from board import Board

class State_search:

    def __init__(self, init_state):
        self.init_state = init_state

    def search_BFS(self):
        visited = {}
        path = []
        open_states = deque()
        open_states.append(self.init_state)
        while open_states:
            cur_state = open_states.popleft()
            if visited[cur_state] is False:
                if cur_state.isSolution():
                   path = self.returnPath(cur_state)
                open_states.extend(cur_state.getNeighbors())
                visited[cur_state] = True
        return path


    def returnPath(self, cur_state):
        return_path = []
        #print("Tutaj return Path")
        return_path.append(cur_state)
        parent = cur_state.getParent()
        while parent is not None:
            return_path.append(parent)
            tmp = parent.getParent()
            parent = tmp
        return return_path

    def search_A_star(self):
        visited = {}
        path = []
        open_states = []
        heapq.heappush(open_states, self.init_state)
        while open_states:
            cur_state = heapq.heappop(open_states)
            #cur_state.getBoard().printBoard()
            #print(cur_state.getHeuristic())
            #print(cur_state.getDepth())
            if cur_state.isSolution():
               # cur_state.getBoard().printBoard()
                path = self.returnPath(cur_state)
                print('tutaj')
                break
            list_key = visited
            #print(list_key)
            if cur_state not in list_key:
                for neighbor in cur_state.getNeighbors():
                    #print(neighbor)
                    #print('----')
                    heapq.heappush(open_states, neighbor)
                # for cos in open_states:
                #     print(cos)
                # print('----------------')
                visited[cur_state] = cur_state
            else:
                if cur_state.getHeuristic() < visited[cur_state].getHeuristic():
                    in_open = visited[cur_state]
                    in_open.setHeuristic(cur_state.getHeuristic())
                    in_open.setParent(cur_state.getParent())
        #for key in visited:
            #print(visited[key].getBoard().printBoard())
            #print(visited[key])

        return path

#open_states = []
#input = [[1, 2, 3], [-1, 4, 6], [7, 5, 8]]
#input_2 = [[1, 2, 3], [4, -1, 6], [7, 5, 8]]
#input_3 = [[1, 2, 3], [7, 4, 6], [-1, 5, 8]]
#goal = [[1, 2, 3], [4, 5, 6], [7, 8, -1]]
#n = 3
#board = Board(n, input)
#board_2= Board(n, input_2)
#board_3 = Board(n, input_3)
#state = State(board, goal, "Misplaces tiles", 0)
#state_2 = State(board_2, goal, "Misplaces tiles", 0)
#state_3 = State(board_3, goal, "Misplaces tiles", 0)
#state.setHeuristicValue()
#heapq.heappush(open_states, state)
#heapq.heappush(open_states, state_2)
#heapq.heappush(open_states, state_3)
#print(heapq.heappop(open_states))
