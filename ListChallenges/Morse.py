# Define a list of Morse codes corresponding to letters from 'a' to 'j'
codes = ['._' , '_…' , '_._.' , '_..' , '.' , '.._.' , '__.' , '….' , '..' , '.___']

# Define the input text to be converted into Morse code
text = 'deface'

# Initialize an empty string to accumulate the Morse code translation
morse_str = ''

# Loop through each character in the input text
for x in text:
    # Convert the character to its corresponding Morse code using its ASCII value
    # ord(x) gives the ASCII value of the character, and subtracting 97 converts it to a 0-based index (for 'a' to 'j')
    morse_str += codes[ord(x)-97] + " "  # Append the Morse code with a space between each letter's code

# Print the final Morse code translation
print(morse_str)
