def second_largest(lst):
    unique_elements = set(lst)
    unique_elements.remove(max(unique_elements))
    return max(unique_elements)

# Example
my_list = [5, 2, 8, 1, 6]
result = second_largest(my_list)
print(result)
