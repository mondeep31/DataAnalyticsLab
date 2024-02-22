def contains_all_vowels(s):
    vowels = set("aeiouAEIOU")
    return set(s) >= vowels

# Example
my_string = "aeiou"
result = contains_all_vowels(my_string)
print(result)
