def find_mirror_characters(s):
    mirror_dict = {'a': 'z', 'b': 'y', 'c': 'x', 'x': 'c', 'y': 'b', 'z': 'a'}
    mirrored_string = ''.join(mirror_dict[char] if char in mirror_dict else char for char in s)
    return mirrored_string

# Example
my_string = "abcxyz"
result = find_mirror_characters(my_string)
print(result)
