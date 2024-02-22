def add_subtract_matrices(mat1, mat2, operation='+'):
    if operation == '+':
        result = [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
    elif operation == '-':
        result = [[mat1[i][j] - mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
    else:
        raise ValueError("Invalid operation. Use '+' for addition or '-' for subtraction.")
    return result

# Example
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
add_result = add_subtract_matrices(matrix1, matrix2, '+')
subtract_result = add_subtract_matrices(matrix1, matrix2, '-')
print("Addition Result:")
print(add_result)
print("Subtraction Result:")
print(subtract_result)
