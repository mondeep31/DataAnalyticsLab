def print_positive_numbers_range(start, end):
    positive_numbers = [num for num in range(start, end+1) if num > 0]
    return positive_numbers

# Example
result = print_positive_numbers_range(-5, 5)
print(result)
