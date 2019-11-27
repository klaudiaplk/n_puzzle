import heapq
import time
from collections import deque


class State_search:

    def __init__(self, init_state):
        self.init_state = init_state
        self.checked_count = 0
        self.used_time = 0.0
        
    def search_BFS(self):
        used_time = time.process_time() 
        self.checked_count = 0
        visited = {}
        path = []
        open_states = deque()
        open_states.append(self.init_state)
        while open_states:
            cur_state = open_states.popleft()
            if cur_state.isSolution():
                   path = self.returnPath(cur_state)
                   self.used_time = time.process_time() - used_time
                   break
            if visited.get(cur_state, False) == False:
                self.checked_count = self.checked_count + 1
                # print checked states
                print("\rChecked states {}".format(self.checked_count), end="")
                open_states.extend(cur_state.getNeighbors())
                visited[cur_state] = True
        print()
        return path


    def returnPath(self, cur_state):
        return_path = []
        return_path.append(cur_state)
        parent = cur_state.getParent()
        while parent is not None:
            return_path.append(parent)
            tmp = parent.getParent()
            parent = tmp
        return return_path

    def search_A_star(self):
        self.checked_count = 0
        used_time = time.process_time() 
        visited = {}
        path = []
        open_states = []
        heapq.heappush(open_states, self.init_state)
        while open_states:
            cur_state = heapq.heappop(open_states)
            if cur_state.isSolution():
                path = self.returnPath(cur_state)
                self.used_time = time.process_time() -used_time
                break
            list_key = visited
            if cur_state not in list_key:
                self.checked_count = self.checked_count + 1
                # print checked states
                print("\rChecked states {}".format(self.checked_count), end="")
                for neighbor in cur_state.getNeighbors():
                    heapq.heappush(open_states, neighbor)
                visited[cur_state] = cur_state
            else:
                if cur_state.getHeuristic() < visited[cur_state].getHeuristic():
                    in_open = visited[cur_state]
                    in_open.setHeuristic(cur_state.getHeuristic())
                    in_open.setParent(cur_state.getParent())
        print()
        return path
    
    def getCheckedCount(self):
        return self.checked_count
    
    def getUsedTime(self):
        return self.used_time
