# Method 1: Using len() function
my_string = "Hello World"
length_method1 = len(my_string)
print(length_method1)

# Method 2: Using loop
length_method2 = 0
for char in my_string:
    length_method2 += 1
print(length_method2)

# Method 3: Using list comprehension
length_method3 = sum(1 for char in my_string)
print(length_method3)

# Method 4: Using recursion
def string_length_recursive(s):
    if not s:
        return 0
    return 1 + string_length_recursive(s[1:])

length_method4 = string_length_recursive(my_string)
print(length_method4)
