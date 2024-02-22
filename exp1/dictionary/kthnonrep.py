from collections import OrderedDict

def kth_non_repeating_char(s, k):
    char_count = OrderedDict.fromkeys(s, 0)
    for char in s:
        char_count[char] += 1

    non_repeating_chars = [char for char, count in char_count.items() if count == 1]
    if len(non_repeating_chars) >= k:
        return non_repeating_chars[k - 1]
    else:
        return "No non-repeating character found."

# Example
my_string = "programming"
k_value = 3
result = kth_non_repeating_char(my_string, k_value)
print(result)
