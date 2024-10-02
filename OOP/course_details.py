class Course:
    def __init__(self, name, dur, *books):
        """
        Initializes the Course instance with a specified name, duration, and suggested books.

        :param name: The name of the course
        :param dur: The duration of the course (in weeks, months, etc.)
        :param books: A variable number of suggested book titles for the course
        """
        self.course_name = name  # Set the course name attribute
        self.duration = dur  # Set the duration attribute
        self.books = [self.Book(b) for b in books]  # Create a list of Book instances

    def show_details(self):
        """Displays the course details including name, duration, and suggested books."""
        print('Name:', self.course_name)  # Print the course name
        print('Duration:', self.duration)  # Print the course duration
        print('Suggested Books')  # Header for the suggested books
        for b in self.books:
            print(b)  # Print each suggested book title

    class Book:
        def __init__(self, title):
            """
            Initializes the Book instance with a specified title.

            :param title: The title of the book
            """
            self.title = title  # Set the title attribute for the Book object

        def __str__(self):
            """Returns the string representation of the book title."""
            return self.title  # Return the title of the book


# Create an instance of the Course class with specific details
c1 = Course('Python', 10, 'Learn Python', 'Python Crash Course')

# Display the course details
c1.show_details()  # Outputs course name, duration, and suggested books
