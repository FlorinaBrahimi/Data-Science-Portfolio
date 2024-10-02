# Prompt the user to enter the distance in kilometers and convert the input to a float
km = float(input('Enter Km: '))

# Convert kilometers to miles using the conversion factor: 1 kilometer = 0.621371 miles
miles = km * 0.621371

# Print the converted distance in miles
# The output will display the miles with the message 'Miles ='
print('Miles =', miles)
