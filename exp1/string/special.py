import string

def contains_special_characters(s):
    special_characters = set(string.punctuation)
    return any(char in special_characters for char in s)

# Example
my_string = "Hello! How are you?"
result = contains_special_characters(my_string)
print(result)
