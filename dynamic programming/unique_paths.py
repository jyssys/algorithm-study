# 완전탐색 (Brute-force)

def bf(r, c): # O(m+n-2Cm-1)
    if r == 0 and c == 0:
        return 1
    
    unique_paths = 0
    
    if r - 1 >= 0:
        unique_paths += bf(r-1, c) # 아래쪽
    if c - 1 >= 0:
        unique_paths += bf(r, c-1) # 오른쪽
    
    return unique_paths


# top-down

def uniquePaths(m, n):
    memo = [[-1] * n for _ in range(m)]

    def td(r, c): # O(M*N)
        if r == 0 and c == 0:
            memo[r][c] = 1
            return memo[r][c]
        
        unique_paths = 0
        
        if memo[r][c] == -1:
            if r - 1 >= 0:
                unique_paths += bf(r-1, c) # 아래쪽
            if c - 1 >= 0:
                unique_paths += bf(r, c-1) # 오른쪽
            memo[r][c] = unique_paths
        return memo[r][c]
    return td(m-1, n-1)

print(uniquePaths(3, 7))

# bottom-up

def bu(m, n):
    memo = [[-1] * n for _ in range(m)]
    
    for r in range(m): # 첫째 열 1로 초기화
        memo[r][0] = 1
    for c in range(n): # 첫째 행 1로 초기화
        memo[0][c] = 1
        
    for r in range(1, m):
        for c in range(1, n):
            memo[r][c] = memo[r-1][c] + memo[r][c-1]
            
    return memo[m-1][n-1]

print(bu(3, 7))