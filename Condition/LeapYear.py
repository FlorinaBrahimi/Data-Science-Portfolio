# Prompt the user to enter a year and convert it to an integer
year = int(input('Enter year'))

# Check if the year is divisible by 100 (i.e., it is a century year)
if year % 100 == 0:
    # If the year is divisible by 100, check if it is also divisible by 400
    if year % 400 == 0:
        # If divisible by 400, it is a leap year
        print('Leap Year')
    else:
        # If not divisible by 400, it is not a leap year
        print('Not a Leap Year')
# If the year is not a century year, check if it is divisible by 4
elif year % 4 == 0:
    # If divisible by 4, it is a leap year
    print('Leap Year')
# If none of the above conditions are met, it is not a leap year
else:
    print('Not a Leap Year')
