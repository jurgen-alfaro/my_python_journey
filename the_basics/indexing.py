# gives access to a sequence's element (str, list, tuples)

name = "jurgen Alfaro!"

if(name[0].islower()):
    name = name.capitalize()

# [start:stop:step]
first_name = name[:6].upper()
last_name = name[7:].lower()
last_character = name[-1]
print(first_name + " " + last_name)
print(last_character)
