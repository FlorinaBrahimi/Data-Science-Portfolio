# Define a recursive generator function 'flatten' that flattens a nested list
def flatten(L):
    # Loop through each element in the list
    for e in L:
        # Check if the element 'e' is iterable (like a list)
        if hasattr(e, '__iter__') and not isinstance(e, str):
            # If it is iterable, recursively flatten it
            yield from flatten(e)
        else:
            # If it's not iterable, yield the element directly
            yield e

# Call the flatten function with a nested list and create a generator
f = flatten([1, 2, [3, [4, 5], 6, 7], 8])

# Print the elements one by one using the 'next' function
print(next(f))  # Output: 1
print(next(f))  # Output: 2
print(next(f))  # Output: 3
print(next(f))  # Output: 4
print(next(f))  # Output: 5
print(next(f))  # Output: 6
print(next(f))  # Output: 7
print(next(f))  # Output: 8
