def unique_values(d):
    unique_values_set = set(val for sublist in d.values() for val in sublist)
    return list(unique_values_set)

# Example
my_dict = {'a': [1, 2, 3], 'b': [2, 3, 4], 'c': [3, 4, 5]}
result = unique_values(my_dict)
print(result)
