# Authors: Samwel, Josephine, Modester
# GitHub handles: @Sammyiel, @Josephine-uwizeye, @Modester-mw

# Question: Make each letter in a string lowercase

# checking space taken to run the program
from memory_profiler import profile


@profile()
# body program
def name():
    input_string = input("What is your name? ")
    print(input_string.lower())


name()

# checking for the time taken
import time

start = time.time()
stop = time.time()
print("Runtime: ", (stop - start), "seconds")

# plotting grapgh for time and space taken
import matplotlib.pyplot as plt

x = [0, 30]
y = [0, 30]
plt.plot(x, y)
plt.xlabel("Time (S)")
plt.ylabel("Memory (MB)")
plt.title("Graph showing time and space taken as input size increases!")
plt.show()
