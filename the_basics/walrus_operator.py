# walrus operator :=

# New to Python 3.8.
# Assignment expression aka walrus operator
# Assigns values to variables as part of a larger expression

# happy = True
# print(happy)

print(happy := True)

# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)

# shorter way
foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)