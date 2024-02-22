def sort_tuples_by_second_item(tuple_list):
    return sorted(tuple_list, key=lambda x: x[1])

# Example
tuple_list = [(1, 4), (3, 2), (5, 1), (2, 7)]
result = sort_tuples_by_second_item(tuple_list)
print(result)
