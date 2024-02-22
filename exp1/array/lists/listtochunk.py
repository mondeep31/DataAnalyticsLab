def chunk_list(lst, chunk_size):
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]

# Example
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = chunk_list(my_list, 3)
print(result)
