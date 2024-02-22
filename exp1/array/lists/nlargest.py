def find_n_largest(lst, n):
    sorted_list = sorted(lst, reverse=True)
    return sorted_list[:n]

# Example
my_list = [5, 2, 8, 1, 6]
result = find_n_largest(my_list, 3)
print(result)
