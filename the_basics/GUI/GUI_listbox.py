# listbox = A widget that holds a list of items

from tkinter import *

def submit():
    food = []
    for i in listbox.curselection():
        food.insert(i, listbox.get(i))
    
    print("You ordered: ")
    for i in food:
        print(i)
    
    
def add():
    listbox.insert(listbox.size(), entry_box.get())
    print("You added: " + entry_box.get())
    listbox.config(height=listbox.size())
    
def delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia", 20),
                  width=12,
                  selectmode=MULTIPLE # SINGLE, BROWSE, MULTIPLE, EXTENDED
                  )
                  
listbox.insert(1, "Pizza") # (index, item)
listbox.insert(2, "Pasta")
listbox.insert(3, "Garlic Bread")
listbox.insert(4, "Soup")
listbox.insert(5, "Salad")

listbox.pack()

listbox.config(
    height=listbox.size(), # size of the listbox | adjusts the height of the listbox to the number of items
)

entry_box = Entry(window,)
entry_box.pack()

submit_button = Button(window, text="Submit", command=submit)
submit_button.pack()

add_button = Button(window, text="Add", command=add)
add_button.pack()

delete_button = Button(window, text="Delete", command=delete)
delete_button.pack()

window.mainloop()