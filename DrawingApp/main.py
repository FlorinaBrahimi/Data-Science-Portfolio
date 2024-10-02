# Import all classes and functions from the tkinter module for GUI creation
from tkinter import *

# Variable to hold the current drawing object
drawing = None

# Function triggered when the user presses the mouse button (first point)
def first_point(e):
    # Set flag to indicate the mouse button is pressed
    pressflag.set(True)
    # Set initial coordinates for the first point
    x1.set(e.x)
    y1.set(e.y)
    # Set the second point to the same coordinates (start drawing from here)
    x2.set(e.x)
    y2.set(e.y)
    # Draw the initial shape based on the first point
    draw_shape()

# Function triggered when the user drags the mouse (update shape during drag)
def dragging(e):
    # If the mouse button is pressed, update the shape's coordinates
    if pressflag.get() == True:
        # Update the shape's coordinates as the mouse moves
        can1.coords(drawing, x1.get(), y1.get(), e.x, e.y)

# Function triggered when the user releases the mouse button (second point)
def second_point(e):
    # Finalize the shape by setting the second point
    can1.coords(drawing, x1.get(), y1.get(), e.x, e.y)
    # Reset the press flag to False (mouse button released)
    pressflag.set(False)

# Function to create and draw the selected shape on the canvas
def draw_shape():
    global drawing
    # List of functions to draw line, rectangle, or oval
    funs = [can1.create_line, can1.create_rectangle, can1.create_oval]
    # If the selected shape is a line
    if shape_var.get() == 0:
        # Draw a line with the specified color and width
        drawing = funs[shape_var.get()](x1.get(), y1.get(), x2.get(), y2.get(),
                                        fill=color_var.get(), width=width_var.get())
    else:
        # Draw a rectangle or oval with the specified outline color and width
        drawing = funs[shape_var.get()](x1.get(), y1.get(), x2.get(), y2.get(),
                                        outline=color_var.get(), width=width_var.get())

# Create the main window
win = Tk()
win.geometry('600x400')

# Create a canvas to draw shapes on
can1 = Canvas(win, bg='#ffffbb')
can1.pack(fill=BOTH, expand=True)

# Bind mouse events for drawing shapes
can1.bind('<ButtonPress>', first_point)    # When the mouse button is pressed
can1.bind('<ButtonRelease>', second_point) # When the mouse button is released
can1.bind('<Motion>', dragging)            # When the mouse is dragged

# Variables to control shape, color, and width
shape_var = IntVar(value=0)        # 0 for line, 1 for rectangle, 2 for oval
color_var = StringVar(value='red') # Default color is red
width_var = IntVar(value=3)        # Default width is 3

# Variables to store the coordinates of the shape
x1 = IntVar(value=0)
y1 = IntVar(value=0)
x2 = IntVar(value=0)
y2 = IntVar(value=0)
pressflag = BooleanVar(value=False) # Flag to track whether the mouse is pressed

# Create a menu bar
menubar = Menu(win)

# Create a shape selection menu
shape_menu = Menu(menubar, tearoff=0)
shape_menu.add_radiobutton(label='Line', variable=shape_var, value=0)
shape_menu.add_radiobutton(label='Rectangle', variable=shape_var, value=1)
shape_menu.add_radiobutton(label='Oval', variable=shape_var, value=2)
menubar.add_cascade(label='Shapes', menu=shape_menu)

# Create a color selection menu
color_menu = Menu(menubar, tearoff=0)
color_menu.add_radiobutton(label='Red', variable=color_var, value='red')
color_menu.add_radiobutton(label='Green', variable=color_var, value='green')
color_menu.add_radiobutton(label='Blue', variable=color_var, value='blue')
menubar.add_cascade(label='Colors', menu=color_menu)

# Create a width selection menu for line thickness
width_menu = Menu(menubar, tearoff=0)
width_menu.add_radiobutton(label='1', variable=width_var, value=1)
width_menu.add_radiobutton(label='3', variable=width_var, value=3)
width_menu.add_radiobutton(label='5', variable=width_var, value=5)
menubar.add_cascade(label='Thickness', menu=width_menu)

# Set the menu bar for the window
win.config(menu=menubar)

# Start the Tkinter event loop
win.mainloop()
