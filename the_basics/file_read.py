
test_file = r"C:\Users\Jurgen_Alfaro\OneDrive - Dell Technologies\Documents\Python\my_python_journey\the_basics\test_folder\test_file.txt"

try:
    with open(test_file) as file:
        print(file.read()) # Hey, I'm a test file!
        
except FileNotFoundError:
    print("That file was not found :(")
    
print(file.closed) # True