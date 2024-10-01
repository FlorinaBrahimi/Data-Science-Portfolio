# 1. Request user input, save the input string in the variable str_manip
str_manip = input("Please enter a sentence: ")

# 2. Calculate and print the length of the string using the len() function
length = len(str_manip)  # Get the length of the input string
print("Length of your sentence is {0} characters".format(length))  # Print the length

# 3. Find the last character of the string and replace it with the '@' character
last_char = str_manip[-1]  # Get the last character of the string
manip_line = str_manip.replace(last_char, "@")  # Replace the last character with '@'
print("Manipulated output1: {0}".format(manip_line))  # Print the manipulated string

# 4. Print the last three letters in reverse order
print("Manipulated output2: {}".format(str_manip[-1:-4:-1]))  # Slice the last three letters and reverse them

# 5. Slice the first three and the last two letters of the string

# 6. Concatenate them and print the result
print("Manipulated output3: {}".format(str_manip[0:3] + str_manip[-2:]))  # Concatenate first three and last two letters and print
