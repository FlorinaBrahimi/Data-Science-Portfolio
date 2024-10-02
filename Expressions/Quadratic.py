# Import the 'math' module to access mathematical functions like square root
import math

# Prompt the user to enter the value of 'a' and convert the input to an integer
a = int(input('Enter a value: '))

# Prompt the user to enter the value of 'b' and convert the input to an integer
b = int(input('Enter b value: '))

# Prompt the user to enter the value of 'c' and convert the input to an integer
c = int(input('Enter c value: '))

# Calculate the first root using the quadratic formula: (-b + sqrt(b^2 - 4ac)) / 2a
root1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)

# Calculate the second root using the quadratic formula: (-b - sqrt(b^2 - 4ac)) / 2a
root2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)

# Print the two roots of the quadratic equation
# The output will display both roots with the message 'Roots are'
print('Roots are', root1, root2)
