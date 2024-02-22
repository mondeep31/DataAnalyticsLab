def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Taking input from the user
num = int(input("Enter a number to find its factorial: "))

# Checking if the input is non-negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print("The factorial of {} is {}".format(num, result))
