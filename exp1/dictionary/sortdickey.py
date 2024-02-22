my_dict = {'b': [20, 30, 40], 'a': [10, 20, 30], 'c': [30, 40, 50]}

# Sorting by keys
sorted_dict_by_keys = dict(sorted(my_dict.items()))
print("Sorted by keys:", sorted_dict_by_keys)

# Sorting by values list
sorted_dict_by_values = {k: sorted(v) for k, v in my_dict.items()}
print("Sorted by values list:", sorted_dict_by_values)
