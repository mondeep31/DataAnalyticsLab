def is_binary_string(s):
    return all(char in '01' for char in s)

# Example
binary_string = "101010101"
result = is_binary_string(binary_string)
print(result)
