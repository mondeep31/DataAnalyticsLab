def rotate_string(s, k):
    return s[k:] + s[:k]

# Example
my_string = "Python"
rotation_count = 2
result = rotate_string(my_string, rotation_count)
print(result)
