def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for ele in lst:
        if ele in seen:
            duplicates.add(ele)
        else:
            seen.add(ele)
    return list(duplicates)

# Example
my_list = [1, 2, 3, 2, 4, 5, 6, 1]
result = find_duplicates(my_list)
print(result)
