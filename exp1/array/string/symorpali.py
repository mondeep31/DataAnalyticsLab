def is_symmetrical(s):
    return s == s[::-1]

# Example
my_string = "radar"
result = is_symmetrical(my_string)
print(result)
