def min_conversion(s1, s2):
    m, n = len(s1), len(s2)
    
    # Create a dp table to store results of subproblems
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill dp[][] in bottom-up manner
    for i in range(m + 1):
        for j in range(n + 1):
            # If first string is empty, only option is to insert all characters of second string
            if i == 0:
                dp[i][j] = j    # Min. operations = j
            
            # If second string is empty, only option is to remove all characters of first string
            elif j == 0:
                dp[i][j] = i    # Min. operations = i
            
            # If last characters are the same, ignore the last character and recur for the remaining substrings
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            
            # If the last character is different, consider all possibilities and find the minimum
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],    # Insert
                                   dp[i - 1][j],    # Remove
                                   dp[i - 1][j - 1]) # Replace
    
    # The value at dp[m][n] contains the minimum number of operations to convert s1 to s2
    return dp[m][n]

# Example usage
s1 = "intention"
s2 = "execution"
print(f"Minimum conversions to transform '{s1}' to '{s2}': {min_conversion(s1, s2)}")
