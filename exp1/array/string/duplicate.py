def replace_duplicate_occurrence(s):
    char_count = {}
    result = []
    for char in s:
        if char in char_count:
            char_count[char] += 1
            result.append(char + str(char_count[char]))
        else:
            char_count[char] = 1
            result.append(char)
    return ''.join(result)

# Example
my_string = "programming"
result = replace_duplicate_occurrence(my_string)
print(result)
