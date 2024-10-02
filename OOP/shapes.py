import math  # Import the math module for mathematical functions and constants

class Shape:
    def __init__(self, name):
        """
        Initializes the Shape instance with a specified name.

        :param name: The name of the shape
        """
        self.name = name  # Set the name attribute for the Shape object

    def area(self):
        """Displays a message indicating that area calculation is for a generic shape."""
        print('Shape area')  # Placeholder method to be overridden by subclasses


class Rectangle(Shape):
    def __init__(self, length, breadth):
        """
        Initializes the Rectangle instance with a specified length and breadth.

        :param length: The length of the rectangle
        :param breadth: The breadth of the rectangle
        """
        super().__init__('Rectangle')  # Call the parent constructor with the shape name
        self.length = length  # Set the length attribute for the Rectangle object
        self.breadth = breadth  # Set the breadth attribute for the Rectangle object

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.length * self.breadth  # Area formula: length * breadth


class Circle(Shape):
    def __init__(self, radius):
        """
        Initializes the Circle instance with a specified radius.

        :param radius: The radius of the circle
        """
        super().__init__('Circle')  # Call the parent constructor with the shape name
        self.radius = radius  # Set the radius attribute for the Circle object

    def area(self):
        """Calculates and returns the area of the circle."""
        return math.pi * (self.radius ** 2)  # Area formula: π * r^2


# Create an instance of the Rectangle class with specific dimensions
r = Rectangle(10, 7)

# Calculate and print the area of the rectangle
print('Area:', r.area())  # Outputs: Area: 70
