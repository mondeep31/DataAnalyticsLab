def max_min_k_elements(my_tuple, k):
    sorted_tuple = sorted(my_tuple)
    max_k_elements = sorted_tuple[-k:]
    min_k_elements = sorted_tuple[:k]
    return max_k_elements, min_k_elements

# Example
my_tuple = (4, 7, 1, 9, 3, 6, 8)
k_value = 3
max_k, min_k = max_min_k_elements(my_tuple, k_value)
print("Max K elements:", max_k)
print("Min K elements:", min_k)
