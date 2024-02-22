def nested_tuple_to_dict(nested_tuple):
    result_dict = {key: value for key, value in nested_tuple}
    return result_dict

# Example
nested_tuple = (('a', 10), ('b', 20), ('c', 30))
result = nested_tuple_to_dict(nested_tuple)
print(result)
