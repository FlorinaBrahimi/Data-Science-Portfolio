class Robot:
    def __init__(self, name):
        """
        Initializes the Robot instance with a specified name.

        :param name: The name of the robot
        """
        self.name = name  # Set the name attribute for the Robot object

    def say_hi(self):
        """Displays a greeting message from the robot."""
        print('Hi, I am ' + self.name)  # Print a greeting message


class PoliceRobot(Robot):
    def say_hi(self):
        """Displays a specialized greeting message for police robots."""
        print('Hi, this is ' + self.name + '. I am here to help you')  # Print a police-specific greeting


# Create an instance of the PoliceRobot class with a specific name
r1 = PoliceRobot('RoboCop')

# Call the say_hi method to display the greeting message
r1.say_hi()
