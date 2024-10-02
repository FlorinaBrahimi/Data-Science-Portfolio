# Prompt the user to enter the length of side 'a' and convert the input to a float
a = float(input('Enter side a: '))

# Prompt the user to enter the length of side 'b' and convert the input to a float
b = float(input('Enter side b: '))

# Prompt the user to enter the height and convert the input to a float
height = float(input('Enter height: '))

# Calculate the area of a trapezoid using the formula: area = 1/2 * (a + b) * height
area = 1/2 * (a + b) * height

# Print the calculated area of the trapezoid
# The output will display the area with the message 'Area is'
print('Area is', area)
