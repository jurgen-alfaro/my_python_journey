from tkinter import *
from tkinter import colorchooser # this is a sub-module of tkinter

def click():
    color = colorchooser.askcolor() # returns a tuple of two values
    print(color) # (RGB color, Hexadecimal color)
    window.config(bg=color[1]) # change the background color of the window
    
    
window = Tk()
window.geometry("420x420")
button = Button(window, command=click, text="Click Me")
button.pack()

window.mainloop()