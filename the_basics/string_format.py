# str.format() = optional method that gives users more control when displaying output

animal = "cow"
item = "moon"

print("The "+ animal + " jumped over the " + item) # Normal output
print("The {} jumped over the {}".format(animal, item)) # Using format fields {}
print("The {0} jumped over the {1}".format(animal, item)) # Positional arguments
print("The {item} jumped over the {animal}".format(animal="cow", item="moon")) # Keyword arguments

text = "The {} jumped over the {}" # An even more "elegant" way to format
print(text.format(animal, item))

# If you want to add some padding/spacing
name = "Jurgen"
print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you!".format(name)) # Padding right
print("Hello, my name is {:<10}. Nice to meet you!".format(name)) # Right-align the value
print("Hello, my name is {:>10}. Nice to meet you!".format(name)) # Left-align the value
print("Hello, my name is {:^10}. Nice to meet you!".format(name)) # Center-align the value

# If you want to add a variable, you can do like this:
print("Hello, my name is {0:10}. Nice to meet you!".format(name)) # Add the variable/value before the :
print("Hello, my name is {name:10}. Nice to meet you!".format(name="Daniel"))

# Format numbers
number = 3.14159
number2 = 1000
print("The number pi is {:.2f}".format(number)) # Display only two digits after the decimal point
print("The number2 is {:,}".format(number2)) # Add a comma to the thousand 
print("The number2 is {:b}".format(number2)) # Display a binary representation
print("The number2 is {:o}".format(number2)) # Display an octal representation
print("The number2 is {:x}".format(number2)) # Display a lowercase hex representation
print("The number2 is {:X}".format(number2)) # Display a uppercase hex representation
print("The number2 is {:e}".format(number2)) # Display in lowercase scientific notation
print("The number2 is {:E}".format(number2)) # Display in uppercase scientific notation