import math  # Import the math module to use mathematical constants and functions

class Circle:
    def __init__(self, radius):
        """
        Initializes the Circle instance with a specified radius.

        :param radius: The radius of the circle
        """
        self.radius = radius  # Set the radius attribute for the Circle object

    def area(self):
        """
        Calculates the area of the circle.

        :return: The area of the circle
        """
        return math.pi * self.radius * self.radius  # Area formula: π * r^2

    def perimeter(self):
        """
        Calculates the perimeter (circumference) of the circle.

        :return: The perimeter of the circle
        """
        return 2 * math.pi * self.radius  # Perimeter formula: 2 * π * r


# Create an instance of the Circle class with a radius of 7
c1 = Circle(7)

# Print the area of the circle
print('Area:', c1.area())

# Print the perimeter of the circle
print('Perimeter:', c1.perimeter())
