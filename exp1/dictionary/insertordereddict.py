from collections import OrderedDict

ordered_dict = OrderedDict([('a', 10), ('b', 20), ('c', 30)])

# Inserting at the beginning
ordered_dict.update({'d': 40})
ordered_dict.move_to_end('d', last=False)
print(ordered_dict)
