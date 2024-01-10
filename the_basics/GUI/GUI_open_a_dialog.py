from tkinter import *
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(title="Open file okay?",
                                           filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))) 
    file = open(file_path, 'r')
    print(file.read())
    file.close()

window = Tk()

button = Button(window, text="Open a file", command=open_file)
button.pack()

window.mainloop()