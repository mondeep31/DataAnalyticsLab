def is_monotonic(arr):
    increasing = decreasing = True
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        if arr[i] < arr[i - 1]:
            increasing = False
    return increasing or decreasing

# Example usage:
array1 = [1, 2, 3, 4, 5]
array2 = [5, 4, 3, 2, 1]

print("Is array1 monotonic?", is_monotonic(array1))
print("Is array2 monotonic?", is_monotonic(array2))
