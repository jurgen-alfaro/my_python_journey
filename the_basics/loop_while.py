# a statement that will execute it’s block of code as long as its condition remains true

name = None

while not name:
    name = input("Enter your name: ")

print("Hello " + name)