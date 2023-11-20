import heapq

graph = {
    'A': [(2, 'B'), (1, 'D')],
    'B': [(1, 'C'), (9, 'E'), (6, 'F')],
    'C': [(4, 'F')],
    'D': [(3, 'C'), (5, 'G')],
    'E': [(1, 'H')],
    'F': [(3, 'E')],
    'G': [(7, 'F'), (9, 'H')],
    'H': []
}

def dijkstra1(graph, start, final):
    costs = {}
    minheap = []
    heapq.heappush(minheap, (0, start))
    
    while minheap:
        cur_cost, cur_v = heapq.heappop(minheap)
        if cur_v not in costs:
            costs[cur_v] = cur_cost
            for cost, next_v in graph[cur_v]:
                next_cost = cur_cost + cost
                heapq.heappush(minheap, (next_cost, next_v))
    
    return costs[final], costs

def dijkstra2(graph, start, final):
    costs = {vertex: float('inf') for vertex in graph}
    prev = {vertex: None for vertex in graph}
    minheap = []
    heapq.heappush(minheap, (0, start))
    costs[start] = 0
    
    while minheap:
        cur_cost, cur_v = heapq.heappop(minheap)
        
        if cur_cost > costs[cur_v]:
            continue
        
        for cost, next_v in graph[cur_v]:
            next_cost = cur_cost + cost
            
            if next_cost < costs[next_v]:
                costs[next_v] = next_cost
                heapq.heappush(minheap, (next_cost, next_v))
                prev[next_v] = cur_v
    
    # 최소 비용과 경로 구성
    path = []
    current = final
    while current is not None:
        path.insert(0, current)
        current = prev[current]
    
    return path


min_cost, costs = dijkstra1(graph, 'A', 'H')
path = dijkstra2(graph, 'A', 'H')

print(f'- 최소 비용 : {min_cost}')
print(f'- Vertex별 최소 비용 : ')
for key, value in costs.items():
    print(f'{key} : {value}')
print(f'- 최적 경로 : {path}')