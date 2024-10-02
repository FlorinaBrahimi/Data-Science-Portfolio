class Computer:
    def __init__(self, name, make, os):
        """
        Initializes the Computer instance with a specified name, CPU make, and OS name.

        :param name: The name of the computer
        :param make: The make of the CPU
        :param os: The name of the operating system
        """
        self.name = name  # Set the name attribute for the Computer object
        self.cpu = self.CPU(make)  # Create an instance of the CPU class
        self.os = self.OS(os)  # Create an instance of the OS class

    def __str__(self):
        """Returns a string representation of the Computer instance."""
        return 'Name: ' + self.name + '\nMake: ' + self.cpu.get_make() + '\nOS Name: ' + self.os.get_name()

    class CPU:
        def __init__(self, make):
            """
            Initializes the CPU instance with a specified make.

            :param make: The make of the CPU
            """
            self.make = make  # Set the make attribute for the CPU object

        def get_make(self):
            """Returns the make of the CPU."""
            return self.make  # Return the make of the CPU

    class OS:
        def __init__(self, os):
            """
            Initializes the OS instance with a specified name.

            :param os: The name of the operating system
            """
            self.name = os  # Set the name attribute for the OS object

        def get_name(self):
            """Returns the name of the operating system."""
            return self.name  # Return the name of the operating system


# Create an instance of the Computer class with specific details
c1 = Computer('PC101', 'Intel', 'Windows')

# Print the details of the computer
print(c1)  # Outputs the computer's name, CPU make, and OS name
