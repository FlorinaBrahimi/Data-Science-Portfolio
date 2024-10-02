# Define two lists L1 and L2
L1 = [3, 5, 12, 6, 4]
L2 = [12, 4, 5, 3, 15, 11, 6]

# Determine the largest length between L1 and L2 using a conditional expression
# If the length of L1 is greater than the length of L2, 'largest' will be the length of L1
# Otherwise, 'largest' will be the length of L2
largest = len(L1) if len(L1) > len(L2) else len(L2)

# Print the largest length
print(largest)
