# *args = parameter that will pack all arguments into a tuple.
# It is useful so that a function can accept a varying amount of arguments

def add(*args): # the * is the most important as it "packs" the arguments into a tuple
    sum = 0
    for i in args: 
        sum += i
    return sum

print(add(1,2,3,4,5,6))