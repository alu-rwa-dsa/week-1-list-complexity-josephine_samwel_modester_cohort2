# Authors: Samwel, Josephine, Modester
# GitHub handles: @Sammyiel, @Josephine-uwizeye, @Modester-mw

# Question: Find the maximum value in a list

# checking space taken to run the program
from memory_profiler import profile


@profile()
# body program with the defined function to find maximum value
def finding_maximum_value():
    list1 = [456, 700, 200, 89900, 920202, 27728, 9, 90, 87, 50, 40, 800000]
    print("Maximum value in a list  : ", max(list1))


finding_maximum_value()

# checking time taken to run the program
import time

start = time.time()
stop = time.time()
print("Runtime: ", (stop - start), "seconds")

# plotting the grapgh of time and space taken
import matplotlib.pyplot as plt

x = [0, 15]
y = [0, 30]
plt.plot(x, y)
plt.xlabel("Time (S)")
plt.ylabel("Memory (MB)")
plt.title("Graph showing time and space taken as input size increases!")
plt.show()
