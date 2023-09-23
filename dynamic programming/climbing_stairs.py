# 으수의 풀이

memo = {1: 1, 2: 2}

# top-down

def climbStairs(n):
    step_case = 0
    
    if n == 1:
        return step_case + 1
    if n == 2:
        return step_case + 2
    
    if n not in memo:
        memo[n] = climbStairs(n-1) + climbStairs(n-2)
    
    return memo[n]

# bottom-up

def climbStairsBU(n):
    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2]

# print(climbStairs(5))

a = [10, 20, 30]
print(a[-1])