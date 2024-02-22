def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Taking input from the user
num = int(input("Enter a number to check if it's prime: "))

# Checking if the number is prime
if is_prime(num):
    print("{} is a prime number.".format(num))
else:
    print("{} is not a prime number.".format(num))
