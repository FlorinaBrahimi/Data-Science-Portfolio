# Prompt the user to enter a day number and convert the input to an integer
day = int(input('Enter Day Number'))

# Check if the day is 1, if so, print 'Sunday'
if day == 1:
    print('Sunday')
# Check if the day is 2, if so, print 'Monday'
elif day == 2:
    print('Monday')
# Check if the day is 3, if so, print 'Tuesday'
elif day == 3:
    print('Tuesday')
# Check if the day is 4, if so, print 'Wednesday'
elif day == 4:
    print('Wednesday')
# Check if the day is 5, if so, print 'Thursday'
elif day == 5:
    print('Thursday')
# Check if the day is 6, if so, print 'Friday'
elif day == 6:
    print('Friday')
# Check if the day is 7, if so, print 'Saturday'
elif day == 7:
    print('Saturday')
# If the input is not between 1 and 7, print 'Invalid Day Number'
else:
    print('Invalid Day Number')
