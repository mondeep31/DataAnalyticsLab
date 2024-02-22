def reverse_array(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array_reversal(arr, k):
    n = len(arr)
    reverse_array(arr, 0, k - 1)
    reverse_array(arr, k, n - 1)
    reverse_array(arr, 0, n - 1)
    return arr

# Example usage:
array = [1, 2, 3, 4, 5]
k = 2
print("Array after rotating by {} positions using reversal algorithm: {}".format(k, rotate_array_reversal(array, k)))
