from random import *  # Import all functions from the random module


class Dice:
    def __init__(self, sides):
        """
        Initializes the Dice instance with a specified number of sides.

        :param sides: The number of sides on the dice
        """
        self.sides = sides  # Set the sides attribute for the Dice object

    def roll_dice(self):
        """
        Rolls the dice and returns a random value between 1 and the number of sides.

        :return: A random integer representing the outcome of the dice roll
        """
        return randint(1, self.sides)  # Generate a random integer from 1 to sides


# Create an instance of the Dice class with 12 sides
d1 = Dice(12)

# Roll the dice and print the result
print(d1.roll_dice())

# Roll the dice again and print the result
print(d1.roll_dice())
