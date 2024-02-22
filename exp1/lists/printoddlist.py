def print_odd_numbers(lst):
    odd_numbers = [num for num in lst if num % 2 != 0]
    return odd_numbers

# Example
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = print_odd_numbers(my_list)
print(result)
