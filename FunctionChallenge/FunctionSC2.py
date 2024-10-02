# Define a function 'pangram' that checks if a given phrase is a pangram
def pangram(phrase):
    # Create a set of all the letters in the English alphabet
    letters = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}

    # Convert the input phrase to a set of characters, which removes duplicates and allows easy comparison
    phrase = set(phrase.lower())  # Convert to lowercase to handle case insensitivity

    # Return True if the set of characters in the phrase contains all the letters in the 'letters' set
    return phrase >= letters

# Test the function with the provided phrase
print(pangram('the quick brown fox jumps over the lazy'))
