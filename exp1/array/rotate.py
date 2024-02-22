def rotate_array(arr, k):
    return arr[k:] + arr[:k]

# Example usage:
array = [1, 2, 3, 4, 5]
k = 2
print("Array after rotating by {} positions: {}".format(k, rotate_array(array, k)))
