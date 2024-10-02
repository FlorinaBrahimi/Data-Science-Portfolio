# Define a list L1 with some duplicate elements
L1 = [3, 5, 7, 9, 3, 6, 5, 2, 3, 7, 10]

# Initialize an empty list L2 to store the unique elements
L2 = []

# Loop through each element in L1
for x in L1:
    # If the current element 'x' is not already in L2, append it to L2
    if x not in L2:
        L2.append(x)

# Print the list L2, which contains only the unique elements from L1
print(L2)
