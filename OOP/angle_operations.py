class Angle:
    def __init__(self, deg):
        """
        Initializes the Angle instance with a specified degree.

        :param deg: The degree of the angle
        """
        self.degree = deg  # Set the degree attribute for the Angle object

    def __add__(self, ang):
        """
        Adds two Angle instances and returns a new Angle instance.

        :param ang: Another Angle instance to add
        :return: A new Angle instance representing the sum of the two angles
        """
        sum = Angle(self.degree + ang.degree)  # Calculate the sum of degrees
        return sum  # Return the new Angle instance

    def __str__(self):
        """Returns a string representation of the Angle instance."""
        return 'Degree ' + str(self.degree)  # Format the angle as a string


# Create instances of the Angle class with specific degrees
a1 = Angle(30)  # First angle
a2 = Angle(45)  # Second angle

# Add the two Angle instances
a3 = a1 + a2  # Resulting angle after addition

# Print the resulting angle
print(a3)  # Outputs: Degree 75
