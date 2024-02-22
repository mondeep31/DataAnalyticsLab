def remove_elements(lst, elements_to_remove):
    return [ele for ele in lst if ele not in elements_to_remove]

# Example
my_list = [1, 2, 3, 4, 5]
elements_to_remove = [2, 4]
result = remove_elements(my_list, elements_to_remove)
print(result)
