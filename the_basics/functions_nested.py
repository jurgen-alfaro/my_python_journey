# These are function calls inside other functions calls. 
# The innermost function calls are resolved first. 
# The returned value is used as argument for the next outer function.

# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

# Nested function
print(round(abs(float(input("Enter a whole positive number: ")))))
