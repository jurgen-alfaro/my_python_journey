# os.remove(<path>)         = delete a file
# os.rmdir(<dir_path>)      = delete an empty directory
# shutil.rmtree(<dir_path>) = delete a directory containing files

import os
import shutil

path = "the_basics\\test_folder\\delete_file.txt"
dir_path = "the_basics\\test_folder\\empty_folder"

try:
    os.remove(path)
    os.rmdir(dir_path)
    shutil.rmtree(dir_path) # USE CAREFULLY!!!
    
except FileNotFoundError:
    print("That file was not found")
    
except PermissionError: # This is when you can't delete an empty folder
    print("You do not have permission to delete that")
    
except OSError: # This is when you can't delete a directory that contains files
    print("The directory cannot be deleted. The directory is not empty!")
    
else:
    print("File '{}' was deleted".format(path))
    print("Dir '{}' was deleted".format(dir_path))