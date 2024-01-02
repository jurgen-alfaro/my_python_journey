# text widget = functions like a text area, you can enter multiple lines of text
from tkinter import *

def submit():
    text = text_area.get("1.0", END) # get all the text from the text area
    print(text)

window = Tk()

text_area = Text(window, 
                 bg="light yellow",
                 font=("Ink Free", 20),
                 height=8, # height in lines
                 width=20, # width in characters
                 padx=20, 
                 pady=20,
                 fg="purple") # foreground color

text_area.pack()

button = Button(window, text="Submit", command=submit)
button.pack()

window.mainloop()
