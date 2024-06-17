def removeKdigits(num, k):
    stack = []
    
    for digit in num:
        while stack and k > 0 and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    # If we still have k digits to remove, remove them from the end
    while k > 0:
        stack.pop()
        k -= 1
    
    # Construct the final number and remove leading zeros
    result = ''.join(stack).lstrip('0')
    
    # If result is empty, return "0"
    return result if result else "0"

# Example usage
num = "1432219"
k = 3
print(removeKdigits(num, k))  # Output: "1219"
