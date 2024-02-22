def remove_tuples_of_length_k(tuple_list, k):
    result = [tup for tup in tuple_list if len(tup) != k]
    return result

# Example
tuple_list = [(1, 2), (3, 4, 5), (6, 7), (8, 9, 10)]
k_value = 2
result = remove_tuples_of_length_k(tuple_list, k_value)
print(result)
