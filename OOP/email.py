""" 
1. Create an email simulator using OOP
2. Use Python file email.py...task is to build out the class, methods, lists, and functions
3. Declare class Email() with the following 
4. Create constructor and pass parameters self, email_address (email address of sender),
   subject_line (subject line), and email_content (contents of email)
5. Add class variable has_been_read, set it to False
6. Class method to edit email...mark_as_read should change has_been_read to True
7. Add empty variable inbox of type list, inbox[]...to store and access email objects
8. Add functions: populate_inbox()..creates an email object with the email address, subject line,
   and contents, and stores it in the inbox and populates your inbox with three sample email objects
9. list_emails()...function loops through the inbox and prints each email's subject_line
   and corresponding number
   Example
   >>0 Welcome to HyperionDev!
   >>1 Great work on the bootcamp!
   >>2 Your excellent marks!
10. [Optional]-- function extended to read, mark as spam, and delete...using the enumerate() function
11. read_email()...function displays a selected email with email_address, subject_line,
    and email_content and sets its has_been_read instance variable to True
12. Use input from user, read_email(i) prints the email stored at position i
13. Index of 0 will print email with the subject line “Welcome to HyperionDev!”
14. Add logic for menu:
    1. Read an email
    2. View unread emails
    3. Quit application

PS. Readability of print outputs in mind, communicate with the user..make clear email read and executed
example: print(f"\nEmail from {email.email_address} marked as read.\n")
"""

### --- OOP Email Simulator with suggested corrections --- ###

# --- Email Class --- #
# Create the Email class, constructor, and methods to create a new Email object.
class Email():
    """Class Email for representing an email"""

    # Declare the class variable 'has_been_read' with a default value of False.
    def __init__(self, email_address, subject_line, email_content):
        """Constructor method for the class Email"""
        self.email_address = email_address  # Store the sender's email address
        self.subject_line = subject_line  # Store the subject line of the email
        self.email_content = email_content  # Store the content of the email
        self.has_been_read = False  # Initialize the email as unread

    # Create the method to change 'has_been_read' from False to True.
    def mark_as_read(self):
        """Method to mark an email as read"""
        self.has_been_read = True  # Set the email's status to read

# --- Lists --- #
# Initialize a class variable as an empty list to store and access the email objects.
    inbox = []  # List to hold email objects

# --- Functions --- #
# Build out the required functions for your program.

# Function that creates 3 sample emails and adds them to the Inbox list. 
def populate_inbox():
    """Function to populate the inbox with emails"""
    emails = [
        Email('abc1@sweden.com', 'Your excellent marks!', 'Very good progress'),  # Sample email 1
        Email('def@finland.com', 'Welcome to HyperionDev!', 'Great work on your application'),  # Sample email 2
        Email('xyz@europe.com', 'Great work on the bootcamp!', 'Well done on your progress')  # Sample email 3
    ]
    Email.inbox.extend(emails)  # Add the sample emails to the inbox list


# Function that prints each email's subject_line along with a corresponding number.
def list_emails():
    """Shows all the emails with subject lines and respective email numbers"""
    print('\nYour Inbox:')  # Header for the inbox
    for i, email in enumerate(Email.inbox):
        print(f'{i}. {email.subject_line}')  # Print the index and subject line of each email


# Create a function that displays a selected email.
# Once displayed, call the class method to set its 'has_been_read' variable to True.
def read_email(index):
    """Displays the selected email that is being passed as an argument"""
    # Check if the index is valid
    if 0 <= index < len(Email.inbox):  # Ensure the index is within the range of the inbox
        email = Email.inbox[index]  # Retrieve the email object at the specified index
        print(f"\nFrom: {email.email_address}")  # Print the sender's email address
        print(f"Subject: {email.subject_line}")  # Print the email's subject line
        print(f"Content: {email.email_content}")  # Print the email's content

        # Mark the email as read
