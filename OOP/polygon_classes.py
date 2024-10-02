import math  # Import the math module to use mathematical functions and constants


class Polygon:
    def __init__(self, ns, *sides):
        """
        Initializes the Polygon instance with a specified number of sides and their lengths.

        :param ns: The number of sides of the polygon
        :param sides: The lengths of the sides of the polygon
        """
        self.no_of_sides = ns  # Set the number of sides attribute
        self.sides = sides[:ns]  # Store only the specified number of sides


class Triangle(Polygon):
    def __init__(self, ns, *sides):
        """
        Initializes the Triangle instance by calling the parent Polygon constructor.

        :param ns: The number of sides (should be 3 for a triangle)
        :param sides: The lengths of the sides of the triangle
        """
        Polygon.__init__(self, ns, *sides)  # Call the parent constructor to initialize the Polygon

    def area(self):
        """Calculates and returns the area of the triangle using Heron's formula."""
        a, b, c = self.sides  # Unpack the lengths of the sides
        s = (a + b + c) / 2  # Calculate the semi-perimeter
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))  # Calculate the area using Heron's formula
        return area  # Return the calculated area


# Create an instance of the Triangle class with specified side lengths
t1 = Triangle(3, 10, 15, 9, 12, 15, 20)

# Calculate and print the area of the triangle
print('Area:', t1.area())
