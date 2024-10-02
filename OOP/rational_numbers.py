class Rational:
    def __init__(self, p, q):
        """
        Initializes the Rational instance with a numerator (p) and a denominator (q).

        :param p: The numerator of the rational number
        :param q: The denominator of the rational number
        """
        self.p = p  # Set the numerator attribute for the Rational object
        self.q = q  # Set the denominator attribute for the Rational object

    def __add__(self, other):
        """
        Adds two Rational instances and returns the result as a new Rational instance.

        :param other: Another Rational instance to add
        :return: A new Rational instance representing the sum
        """
        p = self.p * other.q + self.q * other.p  # Calculate new numerator
        q = self.q * other.q  # Calculate new denominator
        sum = Rational(p, q)  # Create a new Rational instance for the sum
        return sum  # Return the resulting Rational instance

    def __sub__(self, other):
        """
        Subtracts another Rational instance from the current instance and returns the result as a new Rational instance.

        :param other: Another Rational instance to subtract
        :return: A new Rational instance representing the difference
        """
        p = self.p * other.q - self.q * other.p  # Calculate new numerator
        q = self.q * other.q  # Calculate new denominator
        difference = Rational(p, q)  # Create a new Rational instance for the difference
        return difference  # Return the resulting Rational instance

    def __str__(self):
        """Returns a string representation of the Rational instance in the form 'p/q'."""
        return str(self.p) + '/' + str(self.q)  # Format the rational number as a string


# Create instances of the Rational class with specific numerator and denominator values
r1 = Rational(2, 3)
r2 = Rational(1, 2)

# Add the two Rational instances
r3 = r1 + r2

# Print the result of the addition in a formatted string
print(r1, '+', r2, '=', r3)
