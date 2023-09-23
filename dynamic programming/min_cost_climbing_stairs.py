cost = [10, 15, 20, 17, 1]

# recursion 풀이 O(2^n)
def minCostClimb(n):
    if n == 0 or n == 1:
        return 0 # 0 또는 1에서 시작할 수 있음
    
    return min(minCostClimb(n-1) + cost[n-1], minCostClimb(n-2) + cost[n-2])
    # (n-1까지 올라오는 최소비용 + n-1의 비용 : n-1에서 top까지 최소비용) + (n-2까지 올라오는 최소비용 + n-2의 비용 : n-2에서 top까지 최소비용)
    
# top-down DP 풀이 O(n)

memo = {} # memoization

def minCostClimbTD(n):
    if n == 0 or n == 1:
        return 0 # 0 또는 1에서 시작할 수 있음
    
    if n not in memo:
        memo[n] = min(minCostClimbTD(n-1) + cost[n-1], minCostClimbTD(n-2) + cost[n-2])
        
    return memo[n]


# bottom-top DP 풀이 O(n)

memo = {0: 0, 1: 0}

def minCostClimbBT(n):
    if n == 0 or n == 1:
        return 0
    
    for i in range(2, n+1):
        memo[i] = min(memo[i-1] + cost[i-1], memo[i-2] + cost[i-2])
        
    return memo[n]

print(minCostClimbBT(5))