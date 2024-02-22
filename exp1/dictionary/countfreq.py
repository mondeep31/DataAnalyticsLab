def count_frequencies(my_list):
    frequency_dict = {}
    for item in my_list:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    return frequency_dict

# Example
my_list = [1, 2, 3, 1, 2, 3, 4, 5]
result = count_frequencies(my_list)
print(result)
