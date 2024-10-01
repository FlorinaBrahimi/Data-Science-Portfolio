""" 
Program to read a short string and re-create each alternate character as upper and lower case;
and part two, re-creates each alternative word as lower and upper case.
"""

# Get a short sentence from the user and store it in the variable 'short_string'
short_string = input('Enter a short sentence: ')
# Print the captured string to show what the user entered, adding a new line for clarity
print(f'You entered - "{short_string}" \n') 

# Use the enumerate() function to assign indexes to each character in the string
string_enm = enumerate(short_string)

# Using an if...else statement within a for loop, convert even characters to lowercase and odd characters to uppercase
string_alt = ''.join([a.lower() if i % 2 else a.upper() for i, a in enumerate(short_string)])
# Print the output showing the recreated string with alternate upper and lower case characters
print(f'We recreated - "{string_alt}" \n') 

# Part two
# Split the original sentence into words, creating an iterable list of items
string_sp = short_string.split()
# Enumerate the list of words to access both index and word
string_sp_enu = enumerate(string_sp)

# Using an if...else statement within a for loop, convert even indexed words to uppercase and odd indexed words to lowercase
string_up = ' '.join([b.upper() if i % 2 else b.lower() for i, b in enumerate(string_sp)])
# Print the output showing the recreated string with alternate lower and upper case words
print(f'And again - "{string_up}"') 
