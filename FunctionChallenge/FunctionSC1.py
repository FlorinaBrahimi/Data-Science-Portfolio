# Define a function 'minimum' that accepts a variable number of arguments and an optional low_limit parameter
def minimum(*val, low_limit=None):
    # If no low_limit is provided, return the minimum of all the values
    if low_limit is None:
        return min(val)
    else:
        # If low_limit is provided, filter the values to include only those greater than or equal to low_limit
        L = [x for x in val if x >= low_limit]
        # Return the minimum of the filtered list
        return min(L)

# Test the function by passing multiple values and setting a low_limit of 11
print(minimum(1, 2, 5, 10, -5, 12, 20, -10, 25, low_limit=11))
