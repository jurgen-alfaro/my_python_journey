""" SIMPLE CALCULATOR USING PYTHON """
import os

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    RESET = '\033[0m'

def perform_math_operation(num1, num2, op):
    match op:
        case "+": 
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
            
operator = None
num1 = None
num2 = None

os.system("cls") # Clear console screen

print(Color.GREEN + "**** SIMPLE CALCULATOR USING PYTHON ****" + Color.RESET)
while True:
    operator = input("Please enter the operation you want to perform (+ - * /) or 'q' to quit program: ").lstrip().rstrip() # Remove leading & trailing spaces

    if operator.lower() == 'q': 
        print(Color.GREEN + "Have a great day!" + Color.RESET)
        exit(0) # Exit program
        
    if operator == "+" or operator == "-" or operator == "*" or operator == "/":
        while True:
            try:
                num1 = float(input("Enter number 1: "))
                break
            except ValueError:
                print(Color.RED + "That's not a valid number! Please try again." + Color.RESET)
        
        while True:
            try:
                num2 = float(input("Enter number 2: "))
                if(operator == "/" and num2 == 0):
                    print(Color.RED + "Division by 0 not allowed!" + Color.RESET)
                else:
                    break
            except ValueError:
                print(Color.RED + "That's not a valid number! Please try again." + Color.RESET)
        
        print(Color.GREEN + "Result: " + str(perform_math_operation(num1, num2, operator)) + Color.RESET + "\n")
        
            
    
    
        

