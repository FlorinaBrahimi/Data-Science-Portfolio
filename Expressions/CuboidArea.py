# Import the 'math' module to access mathematical functions and constants (like pi)
import math

# Prompt the user to enter the radius of the circle and convert the input to a float
# This ensures the input is treated as a number (floating point) rather than a string
radius = float(input('Enter Radius: '))

# Calculate the area of the circle using the formula: area = π * radius^2
# math.pi provides the value of π and we use ** 2 to square the radius
area = math.pi * radius ** 2

# Print the calculated area of the circle
# The output will display the area with the message 'Area is'
print('Area is', area)
