from os import path
from tkinter import *

def display(): # this function is called when the checkbox is clicked
    if x.get() == 1: # if the checkbox is checked
        print("I agree")
    else: # if the checkbox is not checked
        print("I don't agree")

window = Tk()

x = IntVar() # x is an integer variable because the checkbox returns 0 or 1 

image_path = path.join(__file__, "../python-logo-only.png")  # absolute file path of the image 
photo = PhotoImage(file=image_path)

check_button = Checkbutton(window, 
                           text="I agree to something",
                           variable=x, # the variable that will be changed when the checkbox is clicked
                           onvalue=1, # the value of the variable when the checkbox is checked
                           offvalue=0, # the value of the variable when the checkbox is not checked
                           command=display, # function to be called when the checkbox is clicked
                           font=("Arial", 20), # font family, font size, font style
                           fg="#00FF00", # foreground color
                           bg="#222222", # background color
                           activebackground="#222222", # background color when the checkbox is clicked
                           activeforeground="#00FF00", # foreground color when the checkbox is clicked
                           padx=25, # padding left and right
                           pady=10, # padding top and bottom
                           image=photo, # adds an image to the checkbox
                           compound="left") # creates a checkbox widget

check_button.pack()

window.mainloop()