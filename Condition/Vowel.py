# Prompt the user to enter a lowercase letter and store it in the variable 'ch'
ch = input('Enter a lower case letter')

# Check if the entered character is a vowel (including lowercase 'a', 'e', 'i', 'o', 'u' and an uppercase 'A')
if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A':
    # If the character is a vowel, print 'Vowel'
    print('Vowel')
# If the character is not a vowel, print 'Consonant'
else:
    print('Consonant')
