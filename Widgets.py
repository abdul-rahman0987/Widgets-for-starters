from tkinter import *
from datetime import date


# Create window
root = Tk()
root.title('Getting Started With Widgets')
root.geometry('400x300')


# Add widgets
# Add label
lbl = Label(text = 'Hey There', fg = 'white', bg = 'black', height= 1, width = 300)

# Add name label
name_lbl = Label(text='Full name', bg = 'black')
name_entry = Entry()

# Function to display
def display():
    name = name_entry.get()
    global message
    message = 'Welcome to the application! \nTodays date is: '
    greet = 'Hello'+name+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height= 3)
btn = Button(text='begin', command=display, height = 1, bg = 'green', fg = 'white' )

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()
