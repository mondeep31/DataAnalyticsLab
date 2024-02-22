def split_and_join(s):
    words = s.split()
    joined_string = '-'.join(words)
    return joined_string

# Example
my_string = "Python programming is fun"
result = split_and_join(my_string)
print(result)
