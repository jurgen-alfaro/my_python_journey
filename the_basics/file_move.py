import os

source = "move_file.txt" 
destination = "the_basics\\test_folder\\move_file.txt"

try:
    if os.path.exists(destination): # Make sure to always check if a file with the same name already exists
        print("There is already a file there!")
    else:
        print("Moving {} - Please wait".format(source))
        os.replace(source, destination)
        print("{} was moved".format(source))
    
except FileNotFoundError:
    print("{} was not found".format(source))