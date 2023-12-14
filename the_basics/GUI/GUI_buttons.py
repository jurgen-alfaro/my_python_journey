from os import path
from tkinter import *

count = 0 # count how many times the button was clicked
def click():
    global count # use the global variable count
    count += 1 # increment the count
    print(count) # print the count

window = Tk()
image_path = path.join(__file__, "../thumb-up.png")  # absolute file path of the image 
photo = PhotoImage(file=image_path)

button = Button(window,
                text="Click Me!", # text to be displayed
                command=click, # function to be called when the button is clicked
                font=("Comic Sans", 30, "bold"), # font family, font size, font style
                fg="#00FF00", # foreground color
                bg="#222222", # background color
                activeforeground="#00FF00", # foreground color when the button is clicked
                activebackground="#222222", # background color when the button is clicked
                state="active", # button state: active, disabled, normal
                image=photo, # adds an image to the button
                compound="top") # creates a button widget
button.pack() # adds the button widget to the window, at the center
                
window.mainloop()