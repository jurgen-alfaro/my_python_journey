from tkinter import *
from tkinter import messagebox

def click():
    # messagebox.showinfo(
    #     title="This a title", # Title of the message box
    #     message="This is a message" # Message to display
    # )
    # messagebox.showwarning(title="WARNING!", message="You have a VIRUS!")
    # messagebox.showerror(title="ERROR!", message="You have an ERROR!")
    
    # if messagebox.askokcancel(title="ASK OK CANCEL", message="Are you sure?"): # returns True or False
    #     print("You clicked OK!")
    # else:
    #     print("You clicked Cancel!")
    
    # if messagebox.askretrycancel(title="ASK RETRY CANCEL", message="Do you want to try again?"):
    #     print("You clicked Retry!")
    # else:
    #     print("You clicked Cancel!")
    
    # if messagebox.askyesno(title="ASK YES NO", message="Do you like Python?"):
    #     print("You clicked Yes!")
    # else:
    #     print("You clicked No!")
    
    # answer = messagebox.askquestion(title="ASK QUESTION", message="Do you like Python?") # returns "yes" or "no"
    # if answer == "yes":
    #     print("You clicked Yes!")
    # else:
    #     print("You clicked No!")
    
    answer = messagebox.askyesnocancel(title="ASK YES NO CANCEL", message="Do you like Python?") # returns True, False, or None
    if answer == True:
        print("You clicked Yes!")
    elif answer == False:
        print("You clicked No!")
    else:
        print("You clicked Cancel!")

window = Tk()

button = Button(window,
                command=click,
                text="Click Me")
button.pack()

window.mainloop()