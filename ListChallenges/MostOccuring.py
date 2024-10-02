# Define a list with some repeated elements
L1 = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'A', 'B', 'A']

# Initialize an empty list to store the unique elements and their counts
result = []

# Loop through each element in L1
for x in L1:
    # Count how many times the current element 'x' appears in the list L1
    cnt = L1.count(x)

    # If the tuple (element, count) is not already in the result list, add it
    if (x, cnt) not in result:
        result.append((x, cnt))

# Print the first two elements of the result list (for demonstration purposes)
print(result[0:2])
