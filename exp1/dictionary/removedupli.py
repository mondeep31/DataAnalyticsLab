def remove_duplicate_words(sentence):
    words = sentence.split()
    unique_words = list(set(words))
    return ' '.join(unique_words)

# Example
my_sentence = "Python is great and Python is easy"
result = remove_duplicate_words(my_sentence)
print(result)
