def is_armstrong_number(num):
    # Convert the number to a string to find its length
    num_str = str(num)
    num_digits = len(num_str)
    
    # Calculate the sum of each digit raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum is equal to the original number
    return armstrong_sum == num

# Taking input from the user
num = int(input("Enter a number to check if it's an Armstrong number: "))

# Checking if the number is an Armstrong number
if is_armstrong_number(num):
    print("{} is an Armstrong number.".format(num))
else:
    print("{} is not an Armstrong number.".format(num))
