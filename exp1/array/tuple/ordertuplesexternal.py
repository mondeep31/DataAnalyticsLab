def order_tuples_external_list(tuple_list, order_list):
    return sorted(tuple_list, key=lambda x: order_list.index(x[0]))

# Example
tuple_list = [('b', 4), ('a', 2), ('c', 1), ('d', 3)]
order_list = ['c', 'a', 'b', 'd']
result = order_tuples_external_list(tuple_list, order_list)
print(result)
