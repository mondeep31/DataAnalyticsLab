def interchange_first_last(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

# Example
my_list = [1, 2, 3, 4, 5]
result = interchange_first_last(my_list)
print(result)
