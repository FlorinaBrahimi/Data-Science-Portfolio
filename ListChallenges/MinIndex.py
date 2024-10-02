# Define two lists L1 and L2 containing food items in different orders
L1 = ['pizza', 'nuggets', 'hotdog', 'noodles', 'pasta', 'burger']
L2 = ['burger', 'hotdog', 'noodles', 'pasta', 'nuggets', 'pizza']

# Initialize index1 and index2 with large values to store the indices with the smallest sum later
index1 = 10
index2 = 10

# Loop through each element in L1
for i in range(len(L1)):
    # Find the index of the current L1 item in L2
    indx = L2.index(L1[i])

    # Check if the sum of the indices (i + indx) is less than the current smallest sum (index1 + index2)
    if i + indx < index1 + index2:
        # Update index1 and index2 if a smaller sum is found
        index1 = i
        index2 = indx

# Print the element from L1 that gives the smallest sum of indices, and the sum of the indices
print(L1[index1], index1 + index2)
