# Authors: Samwel, Josephine, Modester
# GitHub handles: @Sammyiel, @Josephine-uwizeye, @Modester-mw

# Question: Sort a list of integers (using the inbuilt python method)
# Given a list of integers, use the .sort() built in method in python to print a sorted list

# checking for space taken
from memory_profiler import profile


@profile()
# body program
def sort_list():
    lst1 = [15, 12, 1, 23, 2, 7]
    lst1.sort(reverse=False)
    print(lst1)


sort_list()

# checking for time taken
import time

start = time.time()
stop = time.time()
print("Runtime: ", (stop - start), "seconds")

# plotting grapgh for time and space taken
import matplotlib.pyplot as plt

x = [0, 15]
y = [0, 30]
plt.plot(x, y)
plt.xlabel("Time (S)")
plt.ylabel("Memory (MB)")
plt.title("Graph showing time and space taken as input size increases!")
plt.show()
