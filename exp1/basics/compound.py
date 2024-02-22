# Function to calculate compound interest
def calculate_compound_interest(principal, rate, time, n):
    amount = principal * (1 + rate/n)**(n*time)
    compound_interest = amount - principal
    return compound_interest

# Taking input from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in percentage): "))
time = float(input("Enter the time period (in years): "))
n = int(input("Enter the number of times interest is compounded per year: "))

# Calculating compound interest using the function
compound_interest = calculate_compound_interest(principal, rate/100, time, n)

# Displaying the result
print("Compound Interest for principal ${}, rate {}%, time {} years, and compounded {} times per year is ${}".format(principal, rate, time, n, compound_interest))
