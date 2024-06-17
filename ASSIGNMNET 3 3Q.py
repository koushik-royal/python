def sum_boundary_elements(matrix):
    if not matrix:
        return 0
    
    M = len(matrix)
    N = len(matrix[0])
    
    if M == 1:
        return sum(matrix[0])
    if N == 1:
        return sum(row[0] for row in matrix)
    
    boundary_sum = 0
    
    # Sum of the first row
    boundary_sum += sum(matrix[0])
    
    # Sum of the last row
    boundary_sum += sum(matrix[M-1])
    
    # Sum of the first column (excluding first and last element if they are already included)
    for i in range(1, M-1):
        boundary_sum += matrix[i][0]
    
    # Sum of the last column (excluding first and last element if they are already included)
    for i in range(1, M-1):
        boundary_sum += matrix[i][N-1]
    
    return boundary_sum

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(sum_boundary_elements(matrix))  
