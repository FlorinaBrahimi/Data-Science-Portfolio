class CurrencyConverter:
    def __init__(self, name, rate):
        """
        Initializes the CurrencyConverter instance with a specified currency name and conversion rate.

        :param name: The name of the currency
        :param rate: The conversion rate of the currency
        """
        self.currency = name  # Set the currency attribute for the CurrencyConverter object
        self.rate = rate  # Set the conversion rate attribute for the CurrencyConverter object

    def get_currency(self):
        """Returns the name of the currency."""
        return self.currency  # Return the currency name

    def get_rate(self):
        """Returns the conversion rate of the currency."""
        return self.rate  # Return the conversion rate

    def set_currency(self, name):
        """
        Sets the name of the currency.

        :param name: The new name of the currency
        """
        self.currency = name  # Update the currency name

    def set_rate(self, rate):
        """
        Sets the conversion rate of the currency.

        :param rate: The new conversion rate
        """
        self.rate = rate  # Update the conversion rate

    def convert(self, amount):
        """
        Converts a specified amount of currency using the conversion rate.

        :param amount: The amount of currency to be converted
        :return: A string representing the conversion result
        """
        return self.currency + ' conversion is ' + str(self.rate * amount)  # Calculate and return the conversion result


# Create an instance of the CurrencyConverter class with specific currency and rate
cc = CurrencyConverter('USD', 70)

# Convert an amount and print the result
print(cc.convert(100))  # Outputs: USD conversion is 7000

# Update the currency and rate
cc.set_currency('AUD')  # Change currency to AUD
cc.set_rate(50)  # Change conversion rate to 50

# Convert an amount with the updated currency and print the result
print(cc.convert(100))  # Outputs: AUD conversion is 5000
