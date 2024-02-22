my_dict = {'b': 20, 'c': 30, 'a': 10}

# Sorting by keys
sorted_dict_by_keys = dict(sorted(my_dict.items()))
print("Sorted by keys:", sorted_dict_by_keys)

# Sorting by values
sorted_dict_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Sorted by values:", sorted_dict_by_values)
