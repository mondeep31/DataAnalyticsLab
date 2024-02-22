def reverse_words(s):
    words = s.split()
    reversed_string = ' '.join(reversed(words))
    return reversed_string

# Example
my_string = "Hello World"
result = reverse_words(my_string)
print(result)
