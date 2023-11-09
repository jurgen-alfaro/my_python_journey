# **kwargs = parameter that will pack all arguments into a dictionary. 
# it is useful so that a function can accept a varying amount of keyword arugments

def hello(**kwargs):
    # print("Hello " + kwargs["first"] + " " + kwargs["last"]) # To access a dictionary element value, use the key name ["key"]
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ") # the 'end=" "' is to print the characters in the same line
        
hello(title="Mr.", first="Jurgen", last="Alfaro", )