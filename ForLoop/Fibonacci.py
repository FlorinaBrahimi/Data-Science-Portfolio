# Prompt the user to enter the number of terms for the Fibonacci sequence and convert the input to an integer
n = int(input('Enter Number of Terms: '))

# Initialize the first two terms of the Fibonacci sequence
a = 0
b = 1

# Loop to generate the Fibonacci sequence up to 'n' terms
for i in range(n):
    # Print the current term in the sequence (initially 'a')
    print(a)
    
    # Calculate the next term in the sequence by adding 'a' and 'b'
    c = a + b
    
    # Update 'a' to the value of 'b' and 'b' to the new calculated term 'c'
    a = b
    b = c
