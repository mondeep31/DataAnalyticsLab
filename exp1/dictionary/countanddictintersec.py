from collections import Counter

def can_make_string(word, target):
    word_counter = Counter(word)
    target_counter = Counter(target)

    intersection = word_counter & target_counter
    return len(target) == sum(intersection.values())

# Example
my_word = "abcef"
my_target = "abc"
result = can_make_string(my_word, my_target)
print(result)
