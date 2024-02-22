def sum_of_values(d):
    return sum(val for val in d.values())

# Example
my_dict = {'a': 10, 'b': 20, 'c': 30}
result = sum_of_values(my_dict)
print(result)
