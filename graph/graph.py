from collections import deque

graph = {
    'A': ['B', 'D', 'E'],
    'B': ['A', 'C', 'D'],
    'C': ['B'],
    'D': ['A', 'B'],
    'E': ['A']
}

def bfs(graph:dict, start_v):
    visited = [start_v]
    queue = deque(start_v)
    
    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    
    return visited

class graphDFS(object):
    def __init__(self, graph = None):
        self.graph = graph
        self.visited = []
    
    def init_visited(self):
        self.visited = []
    
    def dfs(self, start_v):
        self.visited.append(start_v)
        
        for v in self.graph[start_v]:
            if v not in self.visited:
                self.dfs(v)
                
    def bfs(self, start_v):
        self.visited.append(start_v)
        queue = deque(start_v)
        
        while queue:
            cur_v = queue.popleft()
            for v in self.graph[cur_v]:
                if v not in self.visited:
                    self.visited.append(v)
                    queue.append(v)
        
    

# print(bfs(graph, 'A'))
new_graph = graphDFS(graph)
# new_graph.dfs('A')
new_graph.bfs('A')
print(new_graph.visited)