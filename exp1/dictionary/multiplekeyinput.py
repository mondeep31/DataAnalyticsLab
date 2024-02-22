from collections import defaultdict

def create_multikey_dict(keys_values):
    multikey_dict = defaultdict(list)
    for keys, value in keys_values:
        for key in keys:
            multikey_dict[key].append(value)
    return dict(multikey_dict)

# Example
keys_values = [(['a', 'b'], 10), (['b', 'c'], 20), (['a', 'c'], 30)]
result = create_multikey_dict(keys_values)
print(result)
