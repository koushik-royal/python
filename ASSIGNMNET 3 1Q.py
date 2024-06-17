def addBinary(a, b):
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    result = []
    
    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            carry += int(a[i])
            i -= 1
        if j >= 0:
            carry += int(b[j])
            j -= 1
        
        result.append(str(carry % 2))
        carry //= 2
    
    return ''.join(result[::-1])

# Test case
a = "11"
b = "1"
print(addBinary(a, b))  
