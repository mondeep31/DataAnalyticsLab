def sum_of_squares(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."

    # Using the formula for the sum of squares of the first n natural numbers
    result = (n * (n + 1) * (2 * n + 1)) // 6
    return result

# Taking input from the user
n = int(input("Enter a positive integer n: "))

# Calculating the sum of squares using the function
result = sum_of_squares(n)

# Displaying the result
print("The sum of squares of the first {} natural numbers is: {}".format(n, result))
