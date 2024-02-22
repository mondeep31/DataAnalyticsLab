# Method 1: Using del keyword
my_dict = {'a': 10, 'b': 20, 'c': 30}
key_to_remove = 'b'
del my_dict[key_to_remove]
print(my_dict)

# Method 2: Using pop() method
my_dict = {'a': 10, 'b': 20, 'c': 30}
key_to_remove = 'b'
my_dict.pop(key_to_remove, None)
print(my_dict)
