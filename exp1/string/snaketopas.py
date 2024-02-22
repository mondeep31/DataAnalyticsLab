def snake_to_pascal(s):
    words = s.split('_')
    pascal_case = ''.join(word.capitalize() for word in words)
    return pascal_case

# Example
snake_case_string = "python_programming_language"
result = snake_to_pascal(snake_case_string)
print(result)
