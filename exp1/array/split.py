def split_and_add(arr, k):
    return arr[k:] + arr[:k]

# Example usage:
array = [1, 2, 3, 4, 5]
k = 2
print("Array after splitting and adding the first part to the end:", split_and_add(array, k))
