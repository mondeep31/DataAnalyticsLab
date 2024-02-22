def remove_duplicates(s):
    return ''.join(sorted(set(s), key=s.index))

# Example
my_string = "programming"
result = remove_duplicates(my_string)
print(result)
