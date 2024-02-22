def multiply_matrices(mat1, mat2):
    result = [[sum(mat1[i][k] * mat2[k][j] for k in range(len(mat2))) for j in range(len(mat2[0]))] for i in range(len(mat1))]
    return result

# Example
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result = multiply_matrices(matrix1, matrix2)
print(result)
