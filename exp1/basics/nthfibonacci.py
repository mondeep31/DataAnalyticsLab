def nth_fibonacci_number(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
        return fib_sequence[-1]

# Taking input from the user
n = int(input("Enter the value of n to find the n-th Fibonacci number: "))

# Calculating the n-th Fibonacci number using the function
result = nth_fibonacci_number(n)

# Displaying the result
print("The {}-th Fibonacci number is: {}".format(n, result))
