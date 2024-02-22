def add_tuple_to_list(my_list, my_tuple):
    my_list.append(my_tuple)
    return my_list

def add_list_to_tuple(my_tuple, my_list):
    new_tuple = my_tuple + tuple(my_list)
    return new_tuple

# Example
my_list = [(1, 2), (3, 4)]
new_tuple = (5, 6)
result_list = add_tuple_to_list(my_list, new_tuple)
print(result_list)

my_tuple = (1, 2, 3)
new_list = [4, 5, 6]
result_tuple = add_list_to_tuple(my_tuple, new_list)
print(result_tuple)
