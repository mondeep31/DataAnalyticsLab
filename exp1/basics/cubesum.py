def cube_sum(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."

    # Using the formula for the sum of cubes of the first n natural numbers
    result = (n * (n + 1) // 2) ** 2
    return result

# Taking input from the user
n = int(input("Enter a positive integer n: "))

# Calculating the cube sum using the function
result = cube_sum(n)

# Displaying the result
print("The cube sum of the first {} natural numbers is: {}".format(n, result))
