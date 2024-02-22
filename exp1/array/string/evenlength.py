def even_length_words(s):
    words = s.split()
    even_length_words_list = [word for word in words if len(word) % 2 == 0]
    return even_length_words_list

# Example
my_string = "Python is a programming language"
result = even_length_words(my_string)
print(result)
