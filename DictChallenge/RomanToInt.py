# Dictionary mapping Roman numerals to their corresponding decimal values
roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

# Prompt the user to enter a Roman numeral in uppercase letters
number = input('Enter roman number in upper cases')

# Initialize the variable to store the final decimal number
deci_num = 0

# Initialize the index to 0 for iterating through the Roman numeral
i = 0

# Loop through each character of the Roman numeral
while i < len(number):
    # Check if the current numeral is smaller than the next one (to handle cases like IV, IX, etc.)
    if i + 1 < len(number) and roman[number[i]] < roman[number[i + 1]]:
        # If true, subtract the current numeral from the next and add to the total decimal number
        deci_num += roman[number[i + 1]] - roman[number[i]]
        # Skip to the next pair of numerals (since two characters were processed)
        i += 2
    else:
        # If the current numeral is greater or equal to the next one, just add its value to the total
        deci_num += roman[number[i]]
        # Move to the next numeral
        i += 1

# Print the final decimal number
print(deci_num)
