from collections import Counter

def can_frequencies_become_same(my_list):
    frequency_count = Counter(my_list)
    frequency_values = set(frequency_count.values())
    return len(frequency_values) == 1 or (len(frequency_values) == 2 and 1 in frequency_values)

# Example
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
result = can_frequencies_become_same(my_list)
print(result)
