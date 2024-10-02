# Prompt the user to enter John's age and convert the input to a float
john = float(input("Enter John's age"))

# Prompt the user to enter Smith's age and convert the input to a float
smith = float(input("Enter Smith's age"))

# Prompt the user to enter Ajay's age and convert the input to a float
ajay = float(input("Enter Ajay's age"))

# Check if John is older than both Smith and Ajay
if john > smith and john > ajay:
    # If true, print that John is the eldest
    print('John is elder')
# If John is not the eldest, check if Smith is older than Ajay
elif smith > ajay:
    # If true, print that Smith is the eldest
    print('Smith is elder')
# If neither John nor Smith is the eldest, Ajay must be the eldest
else:
    # Print that Ajay is the eldest
    print('Ajay is elder')
