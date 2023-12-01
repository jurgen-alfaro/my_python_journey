# ********************* 
# if __name__ == "__main__":
# *********************

# Python interpreter sets "special variables", one of which is __name__
# Python will assign the __name__ variable a value of "__main__" if the file is being run directly (initial module)

# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules

print(__name__)
if __name__ == "__main__":
    print("Running this module directly")
else: 
    print("Running other module indirectly")