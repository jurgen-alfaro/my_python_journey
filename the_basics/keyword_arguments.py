# These are arguments preceeded by an identifier when we pass them to a function.
# The order of the arguments doesn’t matter, unlike positional arguments.
# Python knows the names of the arguments that our function receives.

# Positional arguments
def hello(first, middle, last):
     print("Hello " + first + " " + middle + " " + last)
    
hello("Jurgen", "Alfaro", "Morera") # If you swap the arguments, the result in the function changes

# Using keyword arguments
hello(last="Morera", first="Jurgen", middle="Alfaro") # The order won't matter


