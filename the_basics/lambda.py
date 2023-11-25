# lambda function = It is a function written in 1 line using lambda keyword. It accepts any number of arguments, but only has one expression. 

# lambda parameters:expression

# def double(x):
#     return x * 2

# print(double(5))

double = lambda x: x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: first_name + " " + last_name
age_check = lambda age: True if age >= 18 else False
print(double(5)) # you need to add the parenthesis
print(multiply(4, 2)) 
print(add(5, 6, 2)) 
print(full_name("Jurgen", "Alfaro")) 
print(age_check(12))