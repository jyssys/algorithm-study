from collections import deque

grid = [
    [0, 0, 0],
    [1, 1, 0],
    [1, 1, 0]
]

class graph(object):
    def __init__(self, graph = None):
        self.graph = graph
        self.visited = []
        
    def init_visited(self):
        self.visited = []
        
    def shortestPath(self):
        delta = [(1,0), (-1,0), (0,1), (0,-1), # 하 상 우 좌
                 (1,1), (1,-1), (-1,1), (-1,0)] # 우하, 좌하, 우상, 좌상
        
        shortest_path_len = -1
        
        row, col = len(self.graph), len(self.graph[0])
        
        # 처음 시작점이 0이 아닐 경우
        if self.graph[0][0] != 0: return shortest_path_len
        # 도착지가 0이 아닐 경우
        if self.graph[row-1][col-1] != 0: return shortest_path_len
    
        self.visited = [[False]*col for _ in range(row)]
        
        self.visited[0][0] = True
        queue = deque()
        queue.append((0, 0, 1)) # row, col, path cnt
        
        while queue:
            cur_row, cur_col, cur_len = queue.popleft()
            
            # 목적지 검사 : 목적지 도착 시 shortest_path_len에 값 저장 후 break
            if cur_row == row - 1 and cur_col == col - 1:
                shortest_path_len = cur_len
                break
            
            # 연결 virtex 확인! 대각선 주의
            for dr, dc in delta:
                next_row = cur_row + dr
                next_col = cur_col + dc
                if next_row >= 0 and next_row < row and next_col >= 0 and next_col < col:
                    if self.graph[next_row][next_col] == 0 and not self.visited[next_row][next_col]:
                        queue.append((next_row, next_col, cur_len + 1))
                        self.visited[next_row][next_col] = True
        
        return shortest_path_len
    
new_maze = graph(grid)
print(new_maze.shortestPath())