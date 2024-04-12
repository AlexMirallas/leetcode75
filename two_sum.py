
def two_sum(nums: list[int], target: int) -> list[int]:
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
            
            
nums = [3,2,3]
target = 6

print(two_sum(nums,target))


