# Prompt the user to enter the bill amount and convert it to a float
amount = float(input('Enter Bill Amount'))

# Check if the bill amount is less than or equal to 1000
if amount <= 1000:
    # If true, apply a 10% discount
    discount = amount * 10 / 100
# Check if the bill amount is greater than 1000 but less than or equal to 5000
elif amount > 1000 and amount <= 5000:
    # If true, apply a 20% discount
    discount = amount * 20 / 100
# Check if the bill amount is greater than 5000 but less than or equal to 10000
elif amount > 5000 and amount <= 10000:
    # If true, apply a 30% discount
    discount = amount * 30 / 100
# If the bill amount is greater than 10000
else:
    # Apply a 50% discount
    discount = amount * 50 / 100

# Calculate the discounted amount to be paid
discamount = amount - discount

# Print the final amount to be paid after applying the discount
print('Pay ', discamount)
