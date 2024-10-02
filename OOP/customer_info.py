class Customer:
    def __init__(self, name, phoneno):
        """
        Initializes the Customer instance with a specified name and phone number.

        :param name: The name of the customer
        :param phoneno: The phone number of the customer
        """
        self.name = name  # Set the name attribute for the Customer object
        self.phneno = phoneno  # Set the phone number attribute for the Customer object

    def get_name(self):
        """Returns the name of the customer."""
        return self.name  # Return the customer's name

    def get_phoneno(self):
        """Returns the phone number of the customer."""
        return self.phneno  # Return the customer's phone number

    def set_phoneno(self, ph):
        """
        Updates the phone number of the customer.

        :param ph: The new phone number to be set
        """
        self.phneno = ph  # Update the phone number attribute


# Create an instance of the Customer class with a name and phone number
c1 = Customer('John', 7650984321)

# Print the customer's name
print('Name:', c1.get_name())

# Print the customer's phone
