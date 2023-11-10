import random # import module

x = random.randint(1, 6) # random num between 1 and 6
y = random.random() # random num between 0 and 1

my_list = ["rock", "paper", "scissors"]
z = random.choice(my_list) # a random choice

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"] # a cards deck
random.shuffle(cards) # shuffles the cards deck

print(x)
print(y)
print(z) 
print(cards)