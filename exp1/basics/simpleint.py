# Function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

# Taking input from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in percentage): "))
time = float(input("Enter the time period (in years): "))

# Calculating simple interest using the function
simple_interest = calculate_simple_interest(principal, rate, time)

# Displaying the result
print("Simple Interest for principal {}, rate {}%, and time {} years is {}".format(principal, rate, time, simple_interest))
