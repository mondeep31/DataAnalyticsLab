def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_in_interval(start, end):
    print("Prime numbers in the interval [{}, {}]: ".format(start, end))
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")

# Taking input for the interval from the user
start_num = int(input("Enter the start of the interval: "))
end_num = int(input("Enter the end of the interval: "))

# Checking if the interval is valid
if start_num >= end_num:
    print("Invalid interval. Please ensure the start is less than the end.")
else:
    # Calling the function to print prime numbers in the interval
    print_primes_in_interval(start_num, end_num)
