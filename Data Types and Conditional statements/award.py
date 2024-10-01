# 1. Request user input for triathlon timings
# 2. Get the timings for swimming, cycling, and running in minutes

swimming = int(input('Enter swim time in minutes: '))  # Input swim time and convert to integer
cycling = int(input('Enter cycling time in minutes: '))  # Input cycling time and convert to integer
running = int(input('Enter running time in minutes: '))   # Input running time and convert to integer

# 3. Add all the numbers to calculate the total triathlon time and print it
triathlon = (swimming + cycling + running)  # Calculate total time
print(f'Total triathlon time in minutes: {triathlon}')  # Print total time

# 4. Check the total time against qualifying conditions
qualifying_time = triathlon  # Store total time in qualifying_time variable
if 0 <= qualifying_time <= 100:  # Check if qualifying time is 100 minutes or less
    print('Qualifying Award for participant is Provincial colours')  # Award for top performance
    
elif 101 <= qualifying_time <= 105:  # Check if qualifying time is between 101 and 105 minutes
    print('Qualifying Award for participant is Provincial half colours')  # Award for good performance

elif 106 <= qualifying_time <= 111:  # Check if qualifying time is between 106 and 111 minutes
    print('Qualifying Award for participant is Provincial scroll')  # Award for average performance

else:  # If the qualifying time is greater than 111 minutes
    print('No award')  # No award given for times above 111 minutes
