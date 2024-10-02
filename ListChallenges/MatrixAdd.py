# Define two 2D lists (matrices), L1 and L2, each with 3 rows and 4 columns
L1 = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
L2 = [[5, 6, 7, 8], [5, 6, 7, 8], [5, 6, 7, 8]]

# Initialize an empty list to store the resulting matrix after addition
L3 = []

# Outer loop iterates over each row (3 rows in total)
for i in range(3):
    # Create a new list to store the sum of elements for the current row
    s = []
    
    # Inner loop iterates over each element in the current row (4 columns in total)
    for j in range(4):
        # Add the corresponding elements from L1 and L2
        r = L1[i][j] + L2[i][j]
        
        # Append the result to the current row list 's'
        s.append(r)
    
    # After processing the entire row, append the row list 's' to the result matrix L3
    L3.append(s)

# Print the resulting matrix L3
print(L3)
