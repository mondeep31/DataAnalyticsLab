def remove_empty_lists(lst):
    return [ele for ele in lst if ele]

# Example
my_list = [1, [], 2, [], 3, []]
result = remove_empty_lists(my_list)
print(result)
