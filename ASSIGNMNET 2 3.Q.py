def find_duplicate(nums):
    # Step 1: Initialize the tortoise and hare
    tortoise = nums[0]
    hare = nums[0]
    
    # Step 2: Find the intersection point of the two runners
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    
    # Step 3: Find the entrance to the cycle
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]
    
    return hare

# Example usage
nums = [1, 3, 4, 2, 2]
print(find_duplicate(nums))  # Output: 2

nums = [3, 1, 3, 4, 2]
print(find_duplicate(nums))  # Output: 3
