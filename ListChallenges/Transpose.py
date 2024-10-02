# Define a 2D list L1, which is a matrix with 3 rows and 4 columns
L1 = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

# Initialize an empty list L2 to store the transposed matrix
L2 = []

# Outer loop: Iterate through each column index of the original matrix (4 columns)
for i in range(4):
    # Create a new list 's' to store the current column elements
    s = []
    
    # Inner loop: Iterate through each row index of the original matrix (3 rows)
    for j in range(3):
        # Append the element at L1[j][i] to 's', which corresponds to transposing the element
        s.append(L1[j][i])
    
    # After gathering a full column as a row, append the list 's' to L2
    L2.append(s)

# Print the transposed matrix L2
print(L2)
