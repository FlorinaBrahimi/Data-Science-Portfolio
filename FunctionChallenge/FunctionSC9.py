# Define a function 'sum0' that takes a list 'L' and sums up the elements divisible by 10
def sum0(L):
    # Initialize a variable 's' to store the sum
    s = 0

    # Loop through each element 'e' in the list 'L'
    for e in L:
        # Check if the element is divisible by 10
        if e % 10 == 0:
            # Add the element to the sum if the condition is met
            s += e

    # Return the final sum
    return s

# Define a list 'L' with some values
L = [100, 123, 200, 234, 350]

# Call the sum0 function and print the result
print(sum0(L))
