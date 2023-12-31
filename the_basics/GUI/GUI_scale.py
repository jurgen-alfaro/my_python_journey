from tkinter import *

def submit():
    print("The temperature is: " + str(scale.get()) + " degrees Celsius.")

window = Tk()

scale = Scale(window,
              from_=0, # minimum value
              to=100, # maximum value
              length=350, # length of the scale
              orient=VERTICAL, # scale orientation
              font=("Consolas", 20), # font family, font size, font style
              tickinterval=10, # numeric indicator for value
              #showvalue=0, # show the value of the scale
              resolution=5, # increments of the scale
              troughcolor="#69EAFF", # color of the scale
              fg="#FF1C00", # color of the text)
              bg="#111111") 

scale.set((scale["from"]-scale["to"])/2 + scale["to"]) # set the initial value of the scale

scale.pack()

button = Button(window, 
                text="Submit",
                command=submit)
button.pack()

window.mainloop()