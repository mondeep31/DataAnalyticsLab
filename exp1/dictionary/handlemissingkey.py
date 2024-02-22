my_dict = {'a': 10, 'b': 20, 'c': 30}

# Handling missing key using get()
key_to_check = 'd'
value = my_dict.get(key_to_check, "Key not found")
print(value)
