from collections import deque

rooms = [[1, 3], [2, 4], [0], [4], [], [3, 4]]

class Rooms(object):
    def __init__(self, rooms = None):
        self.rooms = rooms
        self.visited = []
        
    def init_visited(self):
        self.visited = []
        
    def canVisitAllRoom(self):
        self.visited = [False]*len(self.rooms)
        
        def dfs(v):
            self.visited[v] = True
            for next_v in self.rooms[v]:
                if self.visited[next_v] == False:
                    dfs(next_v)
        
        def bfs(v):
            queue = deque()
            queue.append(v)
            self.visited[v] = True
                        
            while queue:
                cur_v = queue.popleft()
                for next_v in rooms[cur_v]:
                    if self.visited[next_v] == False:
                        queue.append(next_v)
                        self.visited[next_v] = True
        
        dfs(0)
        
        return all(self.visited)

new_rooms = Rooms(rooms)
print(new_rooms.canVisitAllRoom())