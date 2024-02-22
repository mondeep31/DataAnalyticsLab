def print_negative_numbers(lst):
    negative_numbers = [num for num in lst if num < 0]
    return negative_numbers

# Example
my_list = [-2, -1, 0, 1, 2]
result = print_negative_numbers(my_list)
print(result)
