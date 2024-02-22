def print_positive_numbers(lst):
    positive_numbers = [num for num in lst if num > 0]
    return positive_numbers

# Example
my_list = [-2, -1, 0, 1, 2]
result = print_positive_numbers(my_list)
print(result)
