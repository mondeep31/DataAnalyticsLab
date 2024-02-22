def is_palindrome(s):
    return s == s[::-1]

# Example
my_string = "radar"
result = is_palindrome(my_string)
print(result)
