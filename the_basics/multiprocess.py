# ******************************************
# Python multiprocessing module
# ******************************************
# multiprocessing = running tasks in parallel on different CPU cores, bypasses GIL used in threading
# multiprocessing = better for CPU bound tasks (heavy CPU usage)
# multithreading = better for I/O bound tasks (waiting around for I/O)

from multiprocessing import Process, cpu_count # import Process class from multiprocessing module
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    print(cpu_count()) # print number of CPU cores

    a = Process(target=counter, args=(500000000,)) # create a Process object
    b = Process(target=counter, args=(500000000,)) # create a Process object

    a.start() # start the process
    b.start() # start the process

    # Process synchronisation
    a.join() # wait for the process to finish
    b.join() # wait for the process to finish

    print("Finished in: ", time.perf_counter(), "seconds")

if __name__ == "__main__":
    main()