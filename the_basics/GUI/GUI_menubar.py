from os import path
from tkinter import *

folder_path = path.dirname(__file__)

def open_file():
    print("Open a file option was clicked")
    
def save_file():
    print("Save a file option was clicked")    
    
def cut():
    print("Cut option was clicked")

def copy():
    print("Copy option was clicked")

def paste():
    print("Paste option was clicked")


window = Tk()

close_icon = PhotoImage(file=path.join(folder_path, "close_icon.png"))
save_icon = PhotoImage(file=path.join(folder_path, "save_icon.png"))
copy_icon = PhotoImage(file=path.join(folder_path, "content_copy_icon.png"))
folder_open_icon = PhotoImage(file=path.join(folder_path, "folder_open_icon.png"))

menubar = Menu(window)
window.config(menu=menubar) # set the window's menu to the menubar

file_menu = Menu(menubar, tearoff=0, font=("MV Boli", 15))  # tearoff=0 removes the dotted line
menubar.add_cascade(label="File", menu=file_menu) # add the file_menu to the menubar
file_menu.add_command(label="Open", command=open_file, image=folder_open_icon, compound="left") # add a command to the file_menu
file_menu.add_command(label="Save", command=save_file, image=save_icon, compound="left")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit, image=close_icon, compound="left")

edit_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy, image=copy_icon, compound="left")
edit_menu.add_command(label="Paste", command=paste)

window.mainloop()