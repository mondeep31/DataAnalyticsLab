def remove_empty_tuples(lst):
    return [tup for tup in lst if tup]

# Example
my_list = [(1, 2), (), (3, 4), (), (5, 6)]
result = remove_empty_tuples(my_list)
print(result)
