"""Program to read a txt file (DOB.txt) and
split the names & birthdate and print them in separate sections"""

# Open the DOB.txt file in read-only mode using the implicit method
# The encoding is set to "utf-8" to handle any special characters
with open('DOB.txt', 'r', encoding="utf-8") as f:
    # Print a header for the Names section
    print('\nNames\n')
    # Use a for loop to iterate over each line in the file
    for line in f:
        # Split each line into a list of words and store it in 'content'
        content = line.split()
        # Print the first two values from the list, which represent the Names
        print(f"{content[0]} {content[1]}")

# Open the file again to extract Birthdate information
with open('DOB.txt', 'r', encoding="utf-8") as f:
    # Print a header for the Birthdate section
    print('\nBirthdate\n')
    # Use a for loop to iterate over each line in the file
    for dob in f:
        # Split each line into a list of words and store it in 'content'
        content = dob.split()
        # Print the third, fourth, and fifth values from the list, which represent the Birthdate
        print(f"{content[2]} {content[3]} {content[4]}")
