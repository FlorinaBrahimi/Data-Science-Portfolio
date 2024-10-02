# Define two strings, s1 and s2
s1 = 'abc'
s2 = 'xyz'

# Outer loop: Iterate through each character in s1
for i in s1:
    # Inner loop: For each character in s1, iterate through each character in s2
    for j in s2:
        # Print the current characters from s1 and s2 on the same line with a space
        print(i, j, end=' ')
    
    # After printing all combinations of i with characters from s2, move to a new line
    print('')
