from os import path
from tkinter import *

# label = an area widget that holds text and/or an image within a window
# label = used to inform users about something

window = Tk()
image_path = path.join(__file__, "../python-logo-only.png")  # absolute file path of the image 
photo = PhotoImage(file=image_path)

label = Label(window, 
              text="Hello World!", # text to be displayed
              font=("Arial", 40, "bold"), # font family, font size, font style
              fg="#00FF00", # foreground color
              bg="#222222", # background color
              relief="raised", # border style
              bd=10, # border width
              padx=20, # padding left and right
              pady=20, # padding top and bottom
              image=photo, # adds an image to the label
              compound="bottom") # creates a label widget

# label.place(x=0, y=0) # places the label widget at the top left corner of the window
label.pack() # adds the label widget to the window, at the center

window.mainloop()