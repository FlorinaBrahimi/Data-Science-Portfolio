# 1. Request users to input three different numbers
# Step 1: Prompt the user to enter three numbers and convert them to integers
num1 = int(input("Enter number1: "))  # Get the first number from the user
num2 = int(input("Enter number2: "))  # Get the second number from the user
num3 = int(input("Enter number3: "))  # Get the third number from the user

# 2. Calculate the sum of all input numbers and print the result using .format()
print("Sum of all three numbers: {0}".format(num1 + num2 + num3))  # Sum the three numbers and print

# 3. Calculate the difference between num1 and num2 and print the result using .format()
print("Difference of number1 and number2: {0}".format(num1 - num2))  # Subtract num2 from num1 and print

# 4. Multiply num1 and num3 and print the result using .format()
print("Multiplication of number1 and number3: {0}".format(num1 * num3))  # Multiply num1 by num3 and print

# 5. Add all the numbers and then divide by num3, then print the result
print("Sum of three and divide by number3: {0}".format((num1 + num2 + num3) / num3))  # Calculate the sum and divide by num3, then print
