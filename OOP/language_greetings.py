class English:
    def greeting(self):
        """Prints a greeting in English."""
        print('Hello')  # Output greeting in English


class French:
    def greeting(self):
        """Prints a greeting in French."""
        print('Bonjour')  # Output greeting in French


def greet(language):
    """
    Calls the greeting method of the provided language instance.

    :param language: An instance of a class with a greeting method
    """
    language.greeting()  # Call the greeting method of the language object


# Create an instance of the English class
e = English()
# Call the greet function with the English instance
greet(e)  # Outputs: Hello

print('')  # Print a blank line for better readability

# Create an instance of the French class
f = French()
# Call the greet function with the French instance
greet(f)  # Outputs: Bonjour
