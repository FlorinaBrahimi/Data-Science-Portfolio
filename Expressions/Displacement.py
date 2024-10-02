# Prompt the user to enter the initial velocity and convert the input to a float
u = float(input('Enter initial velocity: '))

# Prompt the user to enter the final velocity and convert the input to a float
v = float(input('Enter Final Velocity: '))

# Prompt the user to enter the acceleration and convert the input to a float
a = float(input('Enter Acceleration: '))

# Calculate the displacement using the formula: d = (v^2 - u^2) / (2 * a)
# The formula is derived from the kinematic equation: v^2 = u^2 + 2ad
d = (v**2 - u**2) / (2 * a)

# Print the calculated displacement
# The output will display the displacement with the message 'Displacement is'
print("Displacement is", d)
