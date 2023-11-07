name = "Jurgen"

print(len(name)) # 6 characters
print(name.find("J")) # 0 -> because the J is found at index 0
print(name.capitalize()) # Only capitalizes the first letter of the string
print(name.upper()) # JURGEN
print(name.lower()) # jurgen
print(name.isdigit()) # False
print(name.isalpha()) # True (if there are spaces in the string, it will return False)
print(name.count("r")) # 1 (count how many 'r's are in the string)
print(name.replace("e", "a")) # Jurgan
print(name*3) # JurgenJurgenJurgen