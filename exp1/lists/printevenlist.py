def print_even_numbers(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    return even_numbers

# Example
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = print_even_numbers(my_list)
print(result)
