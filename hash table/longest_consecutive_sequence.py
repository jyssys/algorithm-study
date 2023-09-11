# O(n) 풀이법
def longestConsecutive1(nums):
    longest = 0
    num_dict = {}
    
    for num in nums:
        # O(n)
        num_dict[num] = True
    
    for num in num_dict:
        # O(n) : key값을 순회한다.
        if num - 1 not in num_dict:
            # O(1) : key값을 찾는다.
            cnt = 1
            target = num + 1
            while target in num_dict:
                target += 1
                cnt += 1
            longest = max(longest, cnt)
    return longest

# print(longestConsecutive1([6,7,100,5,4,4]))

# 정렬 풀이법 O(nlog(n))
def longestConsecutive2(nums):
    longest = 0
    num_dict = {}
    
    nums.sort()
    
    for num in nums:
        num_dict[num] = True
        
    for num in num_dict:
        cnt = 1
        target = num + 1
        while target in num_dict:
            target += 1
            cnt += 1
        longest = max(longest, cnt)
    return longest
        
print(longestConsecutive2([]))