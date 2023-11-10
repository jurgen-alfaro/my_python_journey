# copyfile()    = copies contents of a file
# copy()        = copyfile() + permission mode + destination can be a directory
# copy2()       = copy() + copies metadata (file's creation and modification times)

import shutil

src_file = r"C:\Users\Jurgen_Alfaro\OneDrive - Dell Technologies\Documents\Python\my_python_journey\the_basics\test_folder\test_file.txt"
dest = r"C:\Users\Jurgen_Alfaro\OneDrive - Dell Technologies\Documents\Python\my_python_journey\the_basics\test_folder\test_file_copy.txt"

shutil.copyfile(src_file, dest) # src, dest
# shutil.copy(src_file, dest)  
# shutil.copy2(src_file, dest) 