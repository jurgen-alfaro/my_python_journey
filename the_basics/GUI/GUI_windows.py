from os import path
from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

script_dir = path.dirname(__file__)  # absolute directory path of the script
image_path = path.join(script_dir, "python-logo-only.png")  # absolute file path of the image

window = Tk()  # creates a blank window object
window.geometry("420x420")  # sets the size of the window
window.title("GUI Windows")  # sets the title of the window

icon = PhotoImage(file=image_path)  # creates a PhotoImage object to be used as the icon of the window
window.iconphoto(True, icon)  # sets the icon of the window
window.config(bg="#222222")  # sets the background color of the window

window.mainloop()  # keeps the window open until we close it, listen for events


