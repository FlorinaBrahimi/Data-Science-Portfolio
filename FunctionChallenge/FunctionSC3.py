# Define a function 'count' that takes a phrase and counts the number of lowercase and uppercase letters
def count(phrase):
    # Initialize counters for lowercase and uppercase letters
    lower = 0
    upper = 0

    # Loop through each character in the phrase
    for l in phrase:
        # If the character is lowercase, increment the 'lower' counter
        if l.islower():
            lower += 1
        # If the character is uppercase, increment the 'upper' counter
        elif l.isupper():
            upper = upper + 1
    
    # Return the counts of lowercase and uppercase letters
    return lower, upper

# Test the function with the input string 'ABCI'
print(count('ABCI'))
