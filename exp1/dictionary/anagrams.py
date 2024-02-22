def print_anagrams(words):
    anagrams_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams_dict:
            anagrams_dict[sorted_word].append(word)
        else:
            anagrams_dict[sorted_word] = [word]

    for anagram_group in anagrams_dict.values():
        print(anagram_group)

# Example
word_list = ["listen", "silent", "enlist", "hello", "world"]
print_anagrams(word_list)
