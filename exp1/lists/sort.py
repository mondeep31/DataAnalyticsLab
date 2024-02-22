def sort_list_using_another(list1, list2):
    return [x for _, x in sorted(zip(list2, list1))]

# Example
list1 = [1, 2, 3, 4, 5]
list2 = [10, 9, 8, 7, 6]
result = sort_list_using_another(list1, list2)
print(result)
