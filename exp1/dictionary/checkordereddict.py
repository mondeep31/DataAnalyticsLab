from collections import OrderedDict

def check_order(s, pattern):
    pattern_dict = OrderedDict.fromkeys(pattern)
    i = 0
    for char in s:
        if char in pattern_dict:
            if char == list(pattern_dict.keys())[i]:
                i += 1
    return i == len(pattern)

# Example
my_string = "engineers rock"
pattern_to_check = "egr"
result = check_order(my_string, pattern_to_check)
print(result)
