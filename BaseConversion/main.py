from tkinter import *
from tkinter.font import *

def update_label():
    """Update the label text based on the selected number base."""
    # Check which base type is selected and update lbl1 accordingly
    if base_type.get() == 0:  # Decimal
        lbl1['text'] = str(value)  # Display the decimal value
    elif base_type.get() == 1:  # Binary
        lbl1['text'] = str(bin(value))  # Convert to binary and display
    elif base_type.get() == 2:  # Octal
        lbl1['text'] = str(oct(value))  # Convert to octal and display
    elif base_type.get() == 3:  # Hexadecimal
        lbl1['text'] = str(hex(value))  # Convert to hexadecimal and display

# Create the main window
win = Tk()
win.geometry('400x100')  # Set the window size

# Define a font for the radio buttons
fnt = Font(size=15)

# Set the initial value to be displayed
value = 35

# Create a label to display the number
lbl1 = Label(win, text=str(value), font=('Times New Roman', 45), fg='yellow')
lbl1.grid(row=0, column=0, columnspan=4)  # Position the label in the grid

# Create an IntVar to track the selected radio button
base_type = IntVar(value=0)  # Default to Decimal

# Create radio buttons for number base selection
rbn1 = Radiobutton(win, text='Decimal', font=fnt, variable=base_type, value=0, command=update_label)
rbn1.grid(row=1, column=0)  # Position the Decimal radio button

rbn2 = Radiobutton(win, text='Binary', font=fnt, variable=base_type, value=1, command=update_label)
rbn2.grid(row=1, column=1)  # Position the Binary radio button

rbn3 = Radiobutton(win, text='Octal', font=fnt, variable=base_type, value=2, command=update_label)
rbn3.grid(row=1, column=2)  # Position the Octal radio button

rbn4 = Radiobutton(win, text='Hexa Decimal', font=fnt, variable=base_type, value=3, command=update_label)
rbn4.grid(row=1, column=3)  # Position the Hexadecimal radio button

# Start the Tkinter event loop
win.mainloop()
