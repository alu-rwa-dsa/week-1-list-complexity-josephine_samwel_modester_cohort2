# Authors: Samwel, Josephine, Modester
# GitHub handles: @Sammyiel, @Josephine-uwizeye, @Modester-mw

# Question: Implement a basic measure of tracking the time taken to run an algorithm.

# Importing modules
import time

# Identify the starting time
start = time.time()

# The actual program
x = 0

while x < 5000:
    x += 1
    print(x)

# Identify the stop time
stop = time.time()

# Find the difference as the time taken and print
print("Runtime: ", (stop - start), "seconds")
