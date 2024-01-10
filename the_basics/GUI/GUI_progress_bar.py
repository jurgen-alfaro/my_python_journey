from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB = 100
    download = 0
    speed = 1
    while download < GB:
        time.sleep(0.05)
        progress_bar['value'] += (speed/GB*100) 
        download+=speed
        percent.set(str(int((download/GB)*100)) + "%")
        text.set(str(download) + "/" + str(GB) + " GB completed")
        window.update_idletasks() # updates the window
        

window = Tk()

percent = StringVar()
text = StringVar()

progress_bar = Progressbar(window, orient=HORIZONTAL, length=300)
progress_bar.pack(pady=10)

percent_label = Label(window, textvariable=percent).pack()
task_label = Label(window, textvariable=text).pack()

button = Button(window, text="Download", command=start).pack()

window.mainloop()