# Define a custom exception class called NegativeAgeException that inherits from the built-in Exception class
class NegativeAgeException(Exception):
    pass

# Define a function 'stage' to categorize a person's stage of life based on their age
def stage(age):
    # Check if the age is negative, and raise the custom exception if it is
    if age < 0:
        raise NegativeAgeException('Age should not be Negative')
    
    # If age is between 0 and 12, classify the person as a 'Kid'
    elif age >= 0 and age <= 12:
        print('Kid')
    
    # If age is between 13 and 50, classify the person as 'Young'
    elif age >= 13 and age <= 50:
        print('Young')
    
    # If age is greater than or equal to 51, classify the person as 'Old'
    elif age >= 51:
        print('Old')

# Use a try-except block to handle exceptions when calling the 'stage' function
try:
    # Call the stage function with a negative age to trigger the exception
    stage(-160)
    
# Catch the custom NegativeAgeException and store the exception object as 'e'
except NegativeAgeException as e:
    # Print the message from the exception
    print(e)
