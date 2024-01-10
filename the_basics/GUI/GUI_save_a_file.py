from tkinter import *
from tkinter import filedialog

def save_file(): 
    file = filedialog.asksaveasfile(defaultextension=".txt",  # defaultextension is optional
                                    filetypes=(("Text Files", "*.txt"), # filetypes is optional
                                               ("All Files", "*.*"),
                                               ("Python Files", "*.py"),
                                               ("HTML Files", "*.html")),
                                    initialdir="C:/Users/John/Desktop/",) # initialdir is optional                                    
    
    if file is None: # if the user closes the dialog without saving,
        return 
    
    filetext = str(text_area.get(1.0, END))
    file.write(filetext)
    file.close()

window = Tk()

button = Button(window, text="Save a file", command=save_file)
button.pack()
text_area = Text(window, height=10, width=50)
text_area.pack()

window.mainloop()