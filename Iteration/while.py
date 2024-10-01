# 1. Assign variable 'total' to store the sum of the numbers
total = 0

# 2. Assign variable 'count' to store the number of entries
count = 0

# 3. Request user to enter a few numbers and assign the first input to variable 'num'
num = int(input('Enter a few integers and end by typing -1: '))

# 4. Initiate a while loop that continues as long as 'num' is not equal to -1
while num != -1:

# 5. Update 'total' by adding the inputted number 'num'
total += num
    
# 6. Increment 'count' by one to keep track of the number of valid entries
count += 1
    
# 7. Continue asking for input until the user enters -1
num = int(input('Enter a few integers and end by typing -1: '))

# 8. Initiate if condition to check if the user enters -1
if num == -1:

# 9. Calculate the average by dividing total by count and store it in variable 'avg'
avg = total / count
        
# 10. Print the total and average using an f-string and exit the while loop using break
print(f'Total of numbers (excluding -1) entered is {total} and the average is {avg}')
break
