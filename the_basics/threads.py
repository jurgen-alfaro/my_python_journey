# thread = a flow of execution. Like a separate order of instructions.
#       However each thread takes a turn running to achieve concurrency
#       GIL = Global Interpreter Lock
#       Allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#              use multiprocessing

# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)

import threading
import time


def eat_breakfast():
    time.sleep(3) # pretend to do some work
    print('You eat breakfast')

def drink_coffee():
    time.sleep(4) # pretend to do some work
    print('You drink coffee')
    
def study():
    time.sleep(5) # pretend to do some work
    print('You study')

x = threading.Thread(target=eat_breakfast, args=()) # create a thread object
x.start() # start the thread

y = threading.Thread(target=drink_coffee, args=()) # create a thread object
y.start() # start the thread

z = threading.Thread(target=study, args=()) # create a thread object
z.start() # start the thread

# thread synchronisation = is the coordination of threads to complete a task
# thread.join() = wait for thread to finish
x.join() # main thread waits for x to finish
y.join() # main thread waits for y to finish
z.join() # main thread waits for z to finish

# eat_breakfast()
# drink_coffee()
# study()

# Note: These threads are not running in parallel, they are running concurrently
print(threading.active_count()) # 1
print(threading.enumerate()) # [<_MainThread(MainThread, started 140735224659840)>]
print(time.perf_counter()) # will print the time it took to run the program