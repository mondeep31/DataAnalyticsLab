def create_tuple_list(numbers):
    tuple_list = [(num, num**3) for num in numbers]
    return tuple_list

# Example
numbers_list = [1, 2, 3, 4, 5]
result = create_tuple_list(numbers_list)
print(result)
