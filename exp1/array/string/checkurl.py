import re

def contains_url(s):
    pattern = re.compile(r'https?://\S+')
    return bool(pattern.search(s))

# Example
my_string = "Visit our website at https://www.example.com for more information."
result = contains_url(my_string)
print(result)
