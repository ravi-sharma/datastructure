from threading import *
from time import sleep


class first(Thread):
    def run(self):  # using run name as it require in threading
        for i in range(10):
            print('\n Class 1 thread: ', i)
            sleep(1)


class second(Thread):
    def run(self):  # using run name as it require in threading
        for i in range(10):
            print('\n class 2 thread:', i)
            sleep(1)


print('Simple example to see multi threading in python:')

# Initializing objects
object1 = first()
object2 = second()

# In order to run threading we need to call start not run
object1.start()
object2.start()

# Join will let both the threads to complete first then go to next
object1.join()
object2.join()

print('The end!')
