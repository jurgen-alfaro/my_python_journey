from tkinter import *
from tkinter import ttk # gives access to more modern widgets

window = Tk()

notebook = ttk.Notebook(window) # widget that manages a collection of windows and displays one at a time

tab1 = Frame(notebook) # new frame for tab 1
tab2 = Frame(notebook) # new frame for tab 2

notebook.add(tab1, text="Tab 1") # add tab 1 to the notebook
notebook.add(tab2, text="Tab 2") # add tab 2 to the notebook
notebook.pack(expand=True, # expand the notebook to fill the window
              fill="both") # fill the window with the notebook (both x and y directions)

Label(tab1, text="Hello, this is tab 1", width=50, height=25).pack()
Label(tab2, text="Goodbye, this is tab 2", width=50, height=25).pack()

window.mainloop()

