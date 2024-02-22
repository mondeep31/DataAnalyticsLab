from itertools import permutations

def string_permutations(s):
    return [''.join(p) for p in permutations(s)]

# Example
my_string = "abc"
result = string_permutations(my_string)
print(result)
