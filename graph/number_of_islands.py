from collections import deque

island_1 = [
    ['1', '1','0','1','0'],
    ['1', '1','0','0','1'],
    ['0', '0','0','1','0'],
    ['1', '0','1','0','1']
]

class graph(object):
    def __init__(self, graph = None):
        self.graph = graph
        self.visited = []
        
    def init_visited(self):
        self.visited = []
        
    def numIslandsBFS(self):
        number_of_islands = 0
        
        m = len(self.graph) # 행의 개수 : 4
        n = len(self.graph[0]) # 열의 개수 : 5
        
        self.visited = [[False]*n for _ in range(m)]
        
        def bfs(x, y):
            dx = [-1, 1, 0, 0] # 상 하 좌 우 x좌표 변동 시
            dy = [0, 0, -1, 1] # 상 하 좌 우 y좌표 변동 시
            
            self.visited[x][y] = True # bfs에 들어올 경우 해당 좌표는 방문했음
            queue = deque()
            queue.append((x, y)) # value형태가 아니고 암시적 그래프의 좌표기 떄문에 x, y 값 반환
            
            while queue:
                cur_x, cur_y = queue.popleft()
                for i in range(4):
                    next_x = cur_x + dx[i] # 상 하 좌 우 x좌표 변동
                    next_y = cur_y + dy[i] # 상 하 좌 우 y좌표 변동
                    
                    if next_x >= 0 and next_x < m and next_y >= 0 and next_y < n: # 벽이나 모서리에서는 방문이 불가할 수 있음.
                        if self.graph[next_x][next_y] == '1' and not self.visited[next_x][next_y]: # 방문하면 안되는 좌표
                            self.visited[next_x][next_y] = True
                            queue.append((next_x, next_y))
        
        for i in range(m):
            for j in range(n):
                if self.graph[i][j] == '1' and not self.visited[i][j]:
                    bfs(i, j)
                    number_of_islands += 1
                        
        return number_of_islands
    
new_graph = graph(island_1)
print(new_graph.numIslandsBFS())