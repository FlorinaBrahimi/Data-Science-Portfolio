# Define a function 'diff' that checks if the absolute difference between two numbers is <= 5
def diff(n1, n2):
    # Calculate the absolute difference between n1 and n2 and check if it is <= 5
    if abs(n1 - n2) <= 5:
        return True
    else:
        return False

# Test the function by checking the difference between 25 and 15
print(diff(25, 15))
