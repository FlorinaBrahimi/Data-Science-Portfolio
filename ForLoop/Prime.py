# Prompt the user to enter a number and convert it to an integer
n = int(input('Enter a Number: '))

# Initialize a variable 'count' to keep track of the number of divisors of n
count = 0

# Loop through numbers from 1 to n (inclusive) to check for divisors
for i in range(1, n+1):
    # If n is divisible by i (remainder is 0), increase the divisor count
    if n % i == 0:
        count += 1

# If the number has exactly 2 divisors (1 and itself), it is a prime number
if count == 2:
    print('It\'s a Prime')
else:
    # If the number has more than 2 divisors, it is not a prime number
    print('It\'s Not a Prime')
