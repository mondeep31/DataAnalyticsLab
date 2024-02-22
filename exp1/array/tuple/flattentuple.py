def flatten_tuple_of_list(tuple_of_list):
    return tuple(item for sublist in tuple_of_list for item in sublist)

# Example
tuple_of_list = ([1, 2], [3, 4], [5, 6])
result = flatten_tuple_of_list(tuple_of_list)
print(result)
