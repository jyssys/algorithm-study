memo = {1: 1, 2: 1} # memoization (base case 표기 필수)

# top-down dynamic programming

def fibo_td(n):
    if n == 1 or n == 2: # recursion base case
        return 1
    
    if n not in memo:
        memo[n] = fibo_td(n-1) + fibo_td(n-2) # memo dict : key = n, value = fibo value
    return memo[n]

# bottom-up dynamic programming

def fibo_bu(n):
    if n == 1 or n == 2: # recursion base case -> bottom-up에서는 사실상 필요없음.. 재귀가 아니고, base case에서 시작하기 때문
        return 1
    
    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2]
        
    return memo[n]