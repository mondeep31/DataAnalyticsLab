def get_kth_column(matrix, k):
    column = [row[k] for row in matrix]
    return column

# Example
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 1
result = get_kth_column(matrix, k)
print(result)
