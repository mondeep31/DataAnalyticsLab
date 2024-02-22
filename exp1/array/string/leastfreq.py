from collections import Counter

def least_frequent_character(s):
    char_count = Counter(s)
    least_frequent = min(char_count, key=char_count.get)
    return least_frequent

# Example
my_string = "programming"
result = least_frequent_character(my_string)
print(result)
