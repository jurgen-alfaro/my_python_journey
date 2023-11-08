# Scope = The region that a variable is regognized
# A variable is only available from inside the region it is created.
# A global and locally scoped versions of a variable can be created.

name = "Jurgen" # global scope (available inside & outside functions)

def display_name():
    name = "Alfaro" # local scope (available only inside this function)
    print(name)
    
