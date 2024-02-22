def replace_substring(s, old_substring, new_substring):
    return s.replace(old_substring, new_substring)

# Example
my_string = "Python programming is fun and Python is easy"
old_substring = "Python"
new_substring = "Java"
result = replace_substring(my_string, old_substring, new_substring)
print(result)
