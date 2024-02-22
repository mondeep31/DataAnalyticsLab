from collections import Counter

def find_duplicate_characters(s):
    char_count = Counter(s)
    duplicates = [char for char, count in char_count.items() if count > 1]
    return duplicates

# Example
my_string = "programming"
result = find_duplicate_characters(my_string)
print(result)
