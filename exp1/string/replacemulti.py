def replace_words_with_k(s, words, k):
    for word in words:
        s = s.replace(word, k)
    return s

# Example
my_string = "Python programming is fun and Python is easy"
words_to_replace = ["Python", "programming"]
replacement = "K"
result = replace_words_with_k(my_string, words_to_replace, replacement)
print(result)
