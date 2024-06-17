def findDuplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return nums[i]

# Example usage
nums = [1, 3, 4, 2, 2]
print(findDuplicate(nums))  # Output: 2
