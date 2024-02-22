list_of_dicts = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 20}, {'name': 'Charlie', 'age': 30}]

# Sorting by 'age' key
sorted_list = sorted(list_of_dicts, key=lambda x: x['age'])
print(sorted_list)
