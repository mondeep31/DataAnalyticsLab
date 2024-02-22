def remove_ith_character(s, i):
    return s[:i] + s[i+1:]

# Example
my_string = "Python"
index_to_remove = 2
result = remove_ith_character(my_string, index_to_remove)
print(result)
