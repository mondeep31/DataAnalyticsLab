def closest_pair_to_kth_index(my_tuple, k):
    closest_pair = min(my_tuple, key=lambda x: abs(x - k))
    return closest_pair

# Example
my_tuple = (10, 20, 30, 40, 50)
k_value = 35
result = closest_pair_to_kth_index(my_tuple, k_value)
print(result)
