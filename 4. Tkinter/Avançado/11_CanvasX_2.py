from tkinter import *

# Create a canvas widget
canvas = Canvas()
canvas.pack()

# Define functions for drawing lines
def novalinha(e):
    # Get the starting coordinates of the line
    x,y = canvas.canvasx(e.x),canvas.canvasy(e.y)
    # Create a new line with the starting coordinates
    canvas.create_line(x,y,x,y, tags='current')

def estendelinha(e):
    # Get the current coordinates of the line
    x,y = canvas.canvasx(e.x),canvas.canvasy(e.y)
    # Get the current coordinates of the line
    coords = canvas.coords('current')+[x,y]
    # Update the line with the new coordinates
    canvas.coords('current', *coords)

def fechalinha(e):
    # Remove the 'current' tag from the line
    canvas.itemconfig('current', tags=())

# Bind the functions to mouse events
canvas.bind("<Button-1>", novalinha)
canvas.bind("<B1-Motion>", estendelinha)
canvas.bind("<ButtonRelease-1>", fechalinha)

# Start the Tkinter event loop
canvas.pack()
mainloop()
