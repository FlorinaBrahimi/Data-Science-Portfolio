from tkinter import *

def change_color(e):
    """Update the background color of the label based on the RGB values."""
    # Get the current values of the red, green, and blue scales
    r = red_var.get()
    g = green_var.get()
    b = blue_var.get()
    
    # Update the background color of color_lbl using the RGB values in hex format
    color_lbl['bg'] = f'#{r:02x}{g:02x}{b:02x}'  # Format RGB values as hex color code

# Create the main window
win = Tk()
win.geometry('300x200')  # Set the size of the window

# Create a label to display the color
color_lbl = Label(win, text='', bg='black', width=30)
color_lbl.grid(row=0, column=0, columnspan=2)  # Position the color label in the grid

# Create labels for the RGB scales
red_lbl = Label(win, text='Red')
green_lbl = Label(win, text='Green')
blue_lbl = Label(win, text='Blue')

# Position the RGB labels in the grid
red_lbl.grid(row=1, column=0)
green_lbl.grid(row=2, column=0)
blue_lbl.grid(row=3, column=0)

# Create IntVar variables to hold the RGB values, initializing them to 0
red_var = IntVar(value=0)
green_var = IntVar(value=0)
blue_var = IntVar(value=0)

# Create scales for selecting RGB values, linking them to their respective IntVar variables
red_scale = Scale(win, orient=HORIZONTAL, variable=red_var, from_=0, to=255, command=change_color)
green_scale = Scale(win, orient=HORIZONTAL, variable=green_var, from_=0, to=255, command=change_color)
blue_scale = Scale(win, orient=HORIZONTAL, variable=blue_var, from_=0, to=255, command=change_color)

# Position the RGB scales in the grid
red_scale.grid(row=1, column=1)
green_scale.grid(row=2, column=1)
blue_scale.grid(row=3, column=1)

# Start the Tkinter event loop
win.mainloop()
