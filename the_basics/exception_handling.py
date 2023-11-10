# An exception is an event detected during execution that interrupts the flow of a program
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator

except ZeroDivisionError as e:
    print("Exception message: {}".format(e))
    print("You can't divide by zero!")
except ValueError as e:
    print("Exception message: {}".format(e))
    print("Enter only numbers")
except Exception as e: # You can add this at the end in case an unexpected error happens
    print("Exception message: {}".format(e))
    print("Something went wrong")
else: # If there are no exceptions, then print the result
    print(result)
finally: # Whether or not we catch an exception, execute this block of code
    print("This will always execute")
    