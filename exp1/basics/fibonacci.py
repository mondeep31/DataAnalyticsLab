import math

def is_perfect_square(num):
    sqrt_val = int(math.sqrt(num))
    return sqrt_val**2 == num

def is_fibonacci_number(num):
    # A number is a Fibonacci number if and only if one of (5 * n^2 + 4) or (5 * n^2 - 4) is a perfect square
    return is_perfect_square(5 * num**2 + 4) or is_perfect_square(5 * num**2 - 4)

# Taking input from the user
num = int(input("Enter a number to check if it's a Fibonacci number: "))

# Checking if the number is a Fibonacci number
if is_fibonacci_number(num):
    print("{} is a Fibonacci number.".format(num))
else:
    print("{} is not a Fibonacci number.".format(num))
