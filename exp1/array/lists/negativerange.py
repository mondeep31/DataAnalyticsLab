def print_negative_numbers_range(start, end):
    negative_numbers = [num for num in range(start, end+1) if num < 0]
    return negative_numbers

# Example
result = print_negative_numbers_range(-5, 5)
print(result)
