class Orders:
    def __init__(self):
        """Initializes the Orders instance with an empty shopping cart."""
        self.cart = []  # Create an empty list to hold items in the cart

    def add_to_cart(self, item):
        """
        Adds a specified item to the shopping cart.

        :param item: The item to be added to the cart
        """
        self.cart.append(item)  # Append the item to the cart list

    def remove(self, item):
        """
        Removes a specified item from the shopping cart.

        :param item: The item to be removed from the cart
        """
        self.cart.remove(item)  # Remove the item from the cart list

    def __len__(self):
        """Returns the number of items currently in the shopping cart."""
        return len(self.cart)  # Return the length of the cart list

    def __str__(self):
        """Returns a string representation of the current contents of the shopping cart."""
        items = 'Cart Contents: '  # Initialize the string to display cart contents
        for i in self.cart:
            items += i + ', '  # Append each item in the cart to the string
        return items.strip(', ')  # Remove the trailing comma and space


# Create an instance of the Orders class
o = Orders()

# Add items to the shopping cart
o.add_to_cart('Soap')
o.add_to_cart('Paste')
o.add_to_cart('Brush')

# Print the number of items in the cart
print('Cart Size:', len(o))

# Print the current contents of the shopping cart
print(o)

# Remove an item from the shopping cart
o.remove('Paste')

# Print the updated contents of the shopping cart
print(o)
