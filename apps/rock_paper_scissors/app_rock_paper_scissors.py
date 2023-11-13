import os
import random

choices = ["rock", "paper", "scissors"]
icons = {"rock": "🪨", "paper": "📃", "scissors": "✂️"}

os.system("cls") # clear screen

while True:
    computer = random.choice(choices)
    player = None
    
    while player not in choices:
        player = input("Rock, paper, or scissors?: ").lower()

    if player == computer:
        print("Computer:", computer.capitalize(), icons[computer])
        print("Player:", player.capitalize(), icons[player])
        print("Tie! 🤝")

    elif player == "rock":
        if computer == "paper":
            print("Computer:", computer.capitalize(), icons[computer])
            print("Player:", player.capitalize(), icons[player])
            print("You lose! 😞")
            
        if computer == "scissors":
            print("Computer:", computer.capitalize(), icons[computer])
            print("Player:", player.capitalize(), icons[player])
            print("You win! 🎉")
            
    elif player == "scissors":
        if computer == "paper":
            print("Computer:", computer.capitalize(), icons[computer])
            print("Player:", player.capitalize(), icons[player])
            print("You win! 🎉")
            
        if computer == "rock":
            print("Computer:", computer.capitalize(), icons[computer])
            print("Player:", player.capitalize(), icons[player])
            print("You lose! 😞")
            
    elif player == "paper":
        if computer == "rock":
            print("Computer:", computer.capitalize(), icons[computer])
            print("Player:", player.capitalize(), icons[player])
            print("You win! 🎉")
            
        if computer == "scissors":
            print("Computer:", computer.capitalize(), icons[computer])
            print("Player:", player.capitalize(), icons[player])
            print("You lose! 😞")
    
    play_again = input("\nPlay again? (yes/no): ").lower()
    if play_again != "yes":
        break
    else:
        os.system("cls") # clear screen
    
print("Thank you for playing! 😄")
