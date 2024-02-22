from collections import Counter

def word_frequency(s):
    return dict(Counter(s.split()))

# Example
my_string = "Python is fun and Python is easy"
result = word_frequency(my_string)
print(result)
