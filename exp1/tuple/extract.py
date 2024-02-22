def extract_digits_from_tuples(tuple_list):
    digits = [digit for tup in tuple_list for digit in str(tup) if digit.isdigit()]
    return list(map(int, digits))

# Example
tuple_list = [(12, 'abc'), (34, 'def'), (56, 'ghi')]
result = extract_digits_from_tuples(tuple_list)
print(result)
