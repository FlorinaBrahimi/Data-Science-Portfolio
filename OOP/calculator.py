class Calculator:
    """A simple calculator class that performs basic arithmetic operations."""

    @staticmethod
    def add(a, b):
        """
        Adds two numbers and returns the result.

        :param a: The first number
        :param b: The second number
        :return: The sum of a and b
        """
        return a + b  # Return the sum of a and b

    @staticmethod
    def sub(a, b):
        """
        Subtracts the second number from the first and returns the result.

        :param a: The first number
        :param b: The second number
        :return: The difference of a and b
        """
        return a - b  # Return the difference of a and b

    @staticmethod
    def mul(a, b):
        """
        Multiplies two numbers and returns the result.

        :param a: The first number
        :param b: The second number
        :return: The product of a and b
        """
        return a * b  # Return the product of a and b

    @staticmethod
    def div(a, b):
        """
        Divides the first number by the second and returns the result.

        :param a: The numerator
        :param b: The denominator
        :return: The result of a divided by b
        :raises ZeroDivisionError: If b is zero
        """
        return a / b  # Return the quotient of a divided by b


# Example usage
x = 10  # First number
y = 3  # Second number

# Print the result of addition
print(Calculator.add(x, y))  # Outputs: 13

# Print the result of division
print(Calculator.div(x, y))  # Outputs: 3.3333333333333335
