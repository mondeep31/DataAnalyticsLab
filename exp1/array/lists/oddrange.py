def print_odd_numbers_range(start, end):
    odd_numbers = [num for num in range(start, end+1) if num % 2 != 0]
    return odd_numbers

# Example
result = print_odd_numbers_range(1, 10)
print(result)
