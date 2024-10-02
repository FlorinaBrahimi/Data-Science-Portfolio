class Book:
    def __init__(self, title, author, price):
        """
        Initializes the Book instance with a specified title, author, and price.

        :param title: The title of the book
        :param author: The author of the book
        :param price: The price of the book
        """
        self.title = title  # Set the title attribute for the Book object
        self.author = author  # Set the author attribute for the Book object
        self.price = price  # Set the price attribute for the Book object

    def show_details(self):
        """Displays the details of the book."""
        print('Title:', self.title)  # Print the book title
        print('Author:', self.author)  # Print the book author
        print('Price:', self.price)  # Print the book price


# Create instances of the Book class with specific details
b1 = Book('Python Crash Course', 'Eric Matthews', 1000)
b2 = Book('Learn Python', 'Mark Lutz', 500)

# Show details of the first book
b1.show_details()
print('')  # Print a blank line for better readability

# Show details of the second book
b2.show_details()
