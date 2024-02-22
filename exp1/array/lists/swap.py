def swap_elements(lst, pos1, pos2):
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    return lst

# Example
my_list = [1, 2, 3, 4, 5]
result = swap_elements(my_list, 1, 3)
print(result)
