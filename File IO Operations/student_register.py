""" 
Program allows user to register students for an exam venue
Step 1. Asks the user how many students are registering
Step 2. Create a for loop that runs for that number of students
Step 3. Each time the loop runs, the program asks the user to enter the next student ID number. 
Step 4. Write each of the ID numbers to a text file called reg_form.txt
Step 5. Added a dotted line after each student ID in the attendance register, for them to sign
"""

# Use the implicit method to write to the file 'reg_form.txt'
with open("reg_form.txt", "w", encoding="utf-8") as file:
    # Prompt the user to input the exam venue name and write it to the file
    venue = input("Enter exam venue name: ")
    file.write(f"Exam Venue: {venue}\n\n")  # Write venue name with formatting
    
    # Ask the user how many students are registering and store it as an integer
    user = int(input("How many students are registering: "))
    # Write the number of students to the file
    file.write(f"Attendance Register: {user} Students\n\n")  # Write number of students with formatting

    # Use a for loop to input student ID for the required number of students
    # This loop runs 'user' times
    for i in range(user):
        # Prompt the user to enter a student ID number
        student_id = input("Enter a student id number: ")
        # Write the student ID number to the file with an indexed format
        file.write(f"{i + 1}) Student id number: {student_id}\n\n\n")  # Add student ID with index
        
        # Write a dotted line for the student to sign
        file.write("................................................\n\n")  # Dotted line for signature
