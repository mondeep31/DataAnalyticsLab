def find_nth_multiple_in_fibonacci(multiple, n):
    if multiple <= 0 or n <= 0:
        return "Invalid input. Please enter positive integers for both the multiple and n."

    fib_sequence = [0, 1]
    count = 2

    while True:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        if fib_sequence[-1] % multiple == 0:
            count += 1
            if count == n:
                return fib_sequence[-1]

# Taking input from the user
multiple = int(input("Enter the number to find its multiples in the Fibonacci series: "))
n = int(input("Enter the value of n to find the n-th multiple: "))

# Finding the n-th multiple in the Fibonacci series using the function
result = find_nth_multiple_in_fibonacci(multiple, n)

# Displaying the result
print("The {}-th multiple of {} in the Fibonacci series is: {}".format(n, multiple, result))
