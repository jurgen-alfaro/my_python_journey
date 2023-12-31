# radio button = similar to checkbox but only one can be selected at a time
from os import path
from tkinter import *

food = ["Pizza", "Hamburger", "Cake"]
dir_path = path.dirname(__file__)

def order():
    if(x.get() == 0):
        print("You ordered pizza")
    elif(x.get() == 1):
        print("You ordered a hamburger")
    elif(x.get() == 2):
        print("You ordered a cake")
    else:
        print("Huh?")

window = Tk()


pizza_image = PhotoImage(file=path.join(dir_path, "pizza.png"))
hamburguer_image = PhotoImage(file=path.join(dir_path, "hamburger.png"))
cake_image = PhotoImage(file=path.join(dir_path, "cake.png"))
food_images = [pizza_image, hamburguer_image, cake_image]

x = IntVar()

for i in range(len(food)):
    radio_button = Radiobutton(window, 
                               text=food[i], # text of the radio button
                               variable=x, # group of radio buttons if they have the same variable
                               value=i, # assigns a value to the radio button
                               padx=25, # padding left and right
                               font=("Impact", 30), # font family, font size, font style
                               image=food_images[i],
                               compound="left", # add text to the left of the image
                               indicatoron=0,  # eliminates the circle indicator
                               width=375, # width of the radio button
                               command=order) # function to be called when the radio button is clicked
    radio_button.pack(anchor="w") # creates a radio button widget and adds it to the window


window.mainloop()
