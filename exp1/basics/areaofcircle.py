import math

def calculate_circle_area(radius):
    area = math.pi * radius**2
    return area

# Taking input from the user
radius = float(input("Enter the radius of the circle: "))

# Checking if the radius is non-negative
if radius < 0:
    print("Radius cannot be negative. Please enter a non-negative value.")
else:
    # Calculating the area using the function
    circle_area = calculate_circle_area(radius)
    
    # Displaying the result
    print("The area of the circle with radius {} is {:.2f}".format(radius, circle_area))
