from itertools import permutations

def possible_words(characters):
    words = set(''.join(p) for p in permutations(characters))
    return words

# Example
given_characters = "abc"
result = possible_words(given_characters)
print(result)
