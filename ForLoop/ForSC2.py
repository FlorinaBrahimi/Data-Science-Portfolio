# Prompt the user to enter the initial term of the arithmetic sequence and convert it to an integer
a = int(input('Enter initial term: '))

# Prompt the user to enter the common difference of the arithmetic sequence and convert it to an integer
d = int(input('Enter common difference: '))

# Prompt the user to enter the number of terms in the arithmetic sequence and convert it to an integer
n = int(input('Enter number of terms: '))

# Loop through the terms of the arithmetic sequence
# The range starts at 'a' (the initial term) and ends at 'a + n * d' (last term), incrementing by 'd'
for t in range(a, a + n * d, d):
    # Print each term of the arithmetic sequence
    print(t)
