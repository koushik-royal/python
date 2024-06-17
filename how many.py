def smallerNumbersThanCurrent(nums):

    result = [0] * len(nums)
    
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[j] < nums[i]:
                count += 1

        result[i] = count
    
    return result
nums = [8, 1, 2, 2, 3]
print(smallerNumbersThanCurrent(nums))
