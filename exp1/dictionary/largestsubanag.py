from collections import Counter

def largest_anagram_subset(word_list):
    word_count = [Counter(word) for word in word_list]
    common_counter = Counter(word_count[0])

    for word_counter in word_count[1:]:
        common_counter &= word_counter

    return sum(common_counter.values())

# Example
words = ["listen", "silent", "enlist", "hello", "world"]
result = largest_anagram_subset(words)
print(result)
