from tkinter import *

def submit():
    username = entry.get() # get the text from the entry box
    print("Hello " + username)
    entry.config(state=DISABLED) # disable the entry box so it can't be typed in

def delete():
    entry.delete(0, END) # delete from index 0 to the end

def backspace():
    entry.delete(len(entry.get()) - 1, END) # delete the last character in the entry box
    
window = Tk()

entry = Entry(window,
              font=("Arial", 50), # font and size
              fg="#00FF00", # foreground color
              bg="#222222", # background color
              show="*") # hide the text with * (for passwords) 

entry.insert(0, "Enter your name: ") # insert text into the entry box
entry.pack(side=LEFT) # pack it in the window on the left side

submit_button = Button(window, text="submit", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="backspace", command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop() 