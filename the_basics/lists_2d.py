# 2D lists = a list of lists
drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]

print(food) # [['coffee', 'soda', 'tea'], ['pizza', 'hamburger', 'hotdog'], ['cake', 'ice cream']]
print(food[0]) # ['coffee', 'soda', 'tea']
print(food[0][2]) # tea
print(food[1][1]) # hamburger
print(food[2][0]) # cake


