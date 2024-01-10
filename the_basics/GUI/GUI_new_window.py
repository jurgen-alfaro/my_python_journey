from tkinter import *

def create_window():
    new_window = Tk()   # TopLevel() = new window 'on top' of other windows, linked to a 'bottom' window
                                    # Tk() = is the 'bottom' window, is independent of other windows
    old_window.destroy() # destroy the 'bottom' window
    
old_window = Tk()

Button(old_window, text="Open new window", command=create_window).pack()

old_window.mainloop()