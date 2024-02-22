from collections import Counter

def most_frequent_character(s):
    char_count = Counter(s)
    most_frequent = max(char_count, key=char_count.get)
    return most_frequent

# Example
my_string = "programming"
result = most_frequent_character(my_string)
print(result)
