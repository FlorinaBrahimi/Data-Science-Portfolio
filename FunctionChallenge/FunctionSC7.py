# Define a function 'pascal' to print the first 'n' rows of Pascal's Triangle

def pascal(n):
    # Initialize the first row of Pascal's Triangle as [1]
    r = [1]

    # Loop through 'n' rows
    for i in range(n):
        # Print the current row 'r'
        print(r)
        
        # Create a temporary row 'tr' by shifting the current row 'r' one element to the right (i.e., prepend 0)
        tr = [0] + r
        
        # Update the current row 'r' by appending a 0 to the end (i.e., shifting one element to the left)
        r = r + [0]
        
        # Generate the next row by summing corresponding elements from the current row 'r' and the shifted row 'tr'
        r = [x + y for x, y in zip(r, tr)]

# Call the pascal function to generate 6 rows of Pascal's Triangle
pascal(6)
