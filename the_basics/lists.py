# These are used to store multiple items in a single variable

food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]

# useful functions
food.append("ice cream")
food.remove("hotdog")
food.pop() # remove the last element
food.insert(0, "cake") 
food.sort() # sorts alphabetically
food.clear() # clear all the elements of a list

for x in food:
    print(x)