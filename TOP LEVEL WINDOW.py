# Import necessary libraries
from tkinter import *

# Setting up Main Window
root=Tk()
root.geometry("400x300")
root.title("main")

# Function to open the new (top level) window
def topwin():
    # Setting up the top window 
    top = Toplevel()
    top.geometry("180x180")
    top.title("toplevel")
    # Adding a label widget to the Top window
    l2 = Label(top,text = "This is top level window")
    l2.pack()

    top.mainloop()

# Adding a label and button widget to root(main) window
l = Label(root, text = "This is a root window")
btn = Button(root, text = "Click here to open another window ", command = topwin)

# Arrangng Windgets
l.pack()
btn.pack()

root.mainloop()