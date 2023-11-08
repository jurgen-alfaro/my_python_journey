# Slicing is creating a substring by extracting elements from another string.
# [start:stop:step]

name = "Jurgen Alfaro"

# first_name = name[0:6]
first_name = name[:6] # this is the same as above
print(first_name)

# last_name = name[7:13]
last_name = name[7:] # this is the same as above
print(last_name)

# funky_name = name[0:13:3]
funky_name = name[::3] # this is the same as above
print(funky_name)

reversed_name = name[::-1] # this is like counting backwards
print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slicer = slice(7, -4) # this returns a slice object which you can use to slice a string

print(website1[slicer])
print(website2[slicer])


