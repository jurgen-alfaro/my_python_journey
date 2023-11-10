import os

path = r"C:\Users\Jurgen_Alfaro\OneDrive - Dell Technologies\Documents\Python\my_python_journey\the_basics\test_folder\test_file.txt"

# r"some string" the r is for raw string
# you can use double backslash to escape the \ in the path too

# Check if a file exists
if os.path.exists(path):
    print("That location exists!")
    
    if os.path.isfile(path):
        print("That is a file!")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location doesn't exist!")