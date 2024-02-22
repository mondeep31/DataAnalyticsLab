def print_even_numbers_range(start, end):
    even_numbers = [num for num in range(start, end+1) if num % 2 == 0]
    return even_numbers

# Example
result = print_even_numbers_range(1, 10)
print(result)
