# Define a function 'pascal' that generates Pascal's Triangle up to 'n' rows
def pascal(n):
    # Start with the first row of Pascal's Triangle
    r = [1]

    # Loop 'n' times to generate and print 'n' rows
    for i in range(n):
        # Print the current row 'r'
        print(r)
        
        # Create a temporary row 'tr' by adding 0 at the beginning of the current row
        tr = [0] + r
        
        # Add a 0 at the end of the current row 'r'
        r = r + [0]
        
        # Update 'r' by summing adjacent pairs of elements from 'r' and 'tr' to generate the next row
        r = [x + y for x, y in zip(r, tr)]

# Call the pascal function to generate the first 6 rows of Pascal's Triangle
pascal(6)
