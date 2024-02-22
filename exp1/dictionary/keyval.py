def keys_associated_with_values(my_dict, value):
    keys_with_value = [key for key, val in my_dict.items() if val == value]
    return keys_with_value

# Example
my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 20}
target_value = 20
result = keys_associated_with_values(my_dict, target_value)
print(result)
