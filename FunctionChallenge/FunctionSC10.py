# Define a function 'invert' that takes a dictionary 'd' and returns a new dictionary with keys and values swapped
def invert(d):
    # Initialize an empty dictionary to store the inverted key-value pairs
    newd = {}
    
    # Loop through each key-value pair in the original dictionary 'd'
    for k, v in d.items():
        # Assign the value 'v' as the key in 'newd' and the key 'k' as its value
        newd[v] = k
    
    # Return the new inverted dictionary
    return newd

# Define a sample dictionary 'd1'
d1 = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

# Call the invert function on 'd1' and store the result in 'd2'
d2 = invert(d1)

# Print the inverted dictionary
print(d2)
