# A module is a file containing Python code. It may contain functions, classes, etc…
# These are used for modular programming, which is to separate a program into parts. 

#import modules_messages as msg # this is a file in the same base folder
# from modules_messages import * # not recommended if working in big projects
from modules_messages import hello, bye

hello()
bye()

help("modules") # get help with a specific module