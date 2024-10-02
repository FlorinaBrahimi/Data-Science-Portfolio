# Define two lists, L1 and L2
L1 = [10, 15, 6, 9, 12, 8, 4]
L2 = [14, 6, 19 , 4, 7, 10, 11]

# Initialize an empty list to store the common elements
L3 = []

# Loop through each element in L1
for x in L1:
    # Check if the current element 'x' is also in L2
    if x in L2:
        # If it's in both L1 and L2, append it to L3
        L3.append(x)

# Print the list of common elements
print(L3)
