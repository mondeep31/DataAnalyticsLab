def append_keys_values(dict1, dict2):
    result = {}
    for key, value in zip(dict1.keys(), dict2.values()):
        result[key] = value
    return result

# Example
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'x': 40, 'y': 50, 'z': 60}
result = append_keys_values(dict1, dict2)
print(result)
