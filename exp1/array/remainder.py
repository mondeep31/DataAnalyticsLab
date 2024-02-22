def remainder_of_array_multiplication(arr, n):
    result = 1
    for num in arr:
        result = (result * num) % n
    return result

# Example usage:
array = [1, 2, 3, 4, 5]
n = 10
print("Remainder of array multiplication divided by {}: {}".format(n, remainder_of_array_multiplication(array, n)))
