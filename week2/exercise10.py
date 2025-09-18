# Importing is how we bring code from other classes into our code to be able to use them.
# We are importing the sleep function from the time class below.  The sleep function takes a number
# of seconds for the program to sleep (pause).  You can use floating point numbers greater than zero
# as the value for the sleep function.  Values less than 1 will sleep for less than 1 second.
# For example, sleep(0.5) says sleep for 1/2 second (500 milliseconds).
from time import sleep

time_remaining = 5
while time_remaining > 0:
    print(f"Time remaining: {time_remaining} seconds.")
    sleep(1)  # sleep for 1 second
    time_remaining -= 1

print("Time's up!")
