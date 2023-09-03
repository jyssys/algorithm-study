# 시간복잡도 O(n^2) 알고리즘 (완전탐색)

def twoSum1(nums, target):
    n = len(nums)

    for i in range(0, n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return True

    return False

# 시간복잡도 O(nlog(n)) 알고리즘 (정렬 후 탐색)

def twoSum2(nums, target):
    # O(nlog(n))
    nums.sort()
    l, r = 0, len(nums)-1
    
    # O(n)
    while l<r:
        if nums[l] + nums[r] == target: return True
        elif nums[l] + nums[r] > target: r -= 1
        elif nums[l] + nums[r] < target: l += 1
    return False

print(twoSum1(nums=[4, 1, 9, 7, 5, 3, 16], target=14))