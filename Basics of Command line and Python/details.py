# Prompt the user to input their name and store it in the variable 'name'
name = input("What is your name : ")

# Prompt the user to input their age, convert it to an integer, and store it in the variable 'age'
age = int(input("What is your age : "))

# Prompt the user to input their house number, convert it to an integer, and store it in the variable 'house_number'
house_number = int(input("What is your house number : "))

# Prompt the user to input their street name and store it in the variable 'street_name'
street_name = input("What is your street name : ")

# Print a greeting message that includes the user's name, age, house number, and street name
print("Hello {0}! Welcome! You are {1} years old and live at {2} {3}.".format(
    name, age, house_number, street_name))
