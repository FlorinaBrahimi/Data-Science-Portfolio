# 1. Request user to input the pattern size
size = int(input('Enter your pattern size: '))  # Convert user input to an integer

# 2. Set the number of rows to 1
rows = 1

# 3. Calculate the number of columns as size times 2
cols = size * 2  # This ensures that the pattern will have twice the width of the size

# 4. Initiate a for loop with i ranging from rows to columns
for i in range(rows, cols):
    # 5. Assign variable k based on the current value of i
    # If i is less than or equal to size, k is set to i; otherwise, it's set to cols - i
    k = i if i <= size else cols - i  # This determines the number of stars to print in each row

    # 6. Initiate a nested for loop with j ranging from 0 to k
    for j in range(k):
        # 7. Print '*' without a newline, adding a space after each star for formatting
        print('*', end=' ')

    # 8. Print an empty line after finishing the inner loop to move to the next row
    print()
