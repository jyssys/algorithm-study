# O(n)
# 하지만 같은 원소를 두번 사용중임..

def two_sum1(nums, target):
    memo = {}
    for i, value in enumerate(nums):
        memo[value] = 1
        
    for i, value in enumerate(nums):
        needed_number = target - value
        if needed_number in memo:
            # nums가 아닌 memo dictionary에서 해싱함수로 서치하기에 O(1)
            return True
    return False


# 같은 원소 중복 적용 해결.
# 다만 dictionary 특성상 같은 수가 여러개 들어갈 경우에는 풀이가 되지 않음.
        

def two_sum2(nums, target):
    memo = {}
    for index, value in enumerate(nums):
        memo[value] = index
    
    for key, value in memo.items():
        needed_number = target - key
        
        if needed_number in memo and key != needed_number:
            return True
    return False    
        
print(two_sum2([4,1,1,8,2], 2))