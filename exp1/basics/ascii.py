# Taking input from the user
char = input("Enter a character: ")

# Checking if the input is a single character
if len(char) == 1:
    # Obtaining ASCII value using the ord() function
    ascii_value = ord(char)
    print("The ASCII value of '{}' is {}".format(char, ascii_value))
else:
    print("Please enter a single character.")
