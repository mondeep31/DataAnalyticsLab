def sum_of_digits(lst):
    return [sum(map(int, str(num))) for num in lst]

# Example
my_list = [12, 34, 56, 78]
result = sum_of_digits(my_list)
print(result)
