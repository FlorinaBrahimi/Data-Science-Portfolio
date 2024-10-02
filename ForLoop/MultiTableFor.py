# Prompt the user to enter a number and convert the input to an integer
n = int(input('Enter a Number: '))

# Loop through the numbers from 1 to 10 (inclusive) to generate the multiplication table for 'n'
for count in range(1, 11):
    # Print the multiplication result in the format: n X count = product
    print(n, 'X', count, '=', count * n)
