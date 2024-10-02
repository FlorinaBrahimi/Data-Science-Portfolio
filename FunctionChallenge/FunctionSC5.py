# Define a function 'max3' that returns the maximum of three numbers
def max3(a, b, c):
    # If 'a' is greater than both 'b' and 'c', return 'a' as the maximum
    if a > b and a > c:
        return a
    # If 'b' is greater than 'c', return 'b' as the maximum
    elif b > c:
        return b
    # If neither of the above conditions are met, return 'c' as the maximum
    else:
        return c

# Test the function with the input (12, 12, 12)
print(max3(12, 12, 12))
