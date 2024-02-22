from functools import reduce
import operator

def multiply_elements(lst):
    return reduce(operator.mul, lst, 1)

# Example
my_list = [1, 2, 3, 4, 5]
result = multiply_elements(my_list)
print(result)
