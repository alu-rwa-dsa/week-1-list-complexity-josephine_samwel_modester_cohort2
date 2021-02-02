# Authors: Samwel, Josephine, Modester
# GitHub handles: @Sammyiel, @Josephine-uwizeye, @Modester-mw

# Question: Implement a basic measure of tracking the space taken to run an algorithm.

#This project would receive inputs from the user, as number of students per class and it
# calculates the number of desks the school should buy given that each desk can accommodate at most 2 number of students.


#import module for tracking memory usage
from memory_profiler import profile

#decorating the function
@profile()

# program body starts
def maths_calc():

    no_class1 = int(input("Number of students in the first class"))
    no_class2 = int(input("Number of student in the second class"))
    no_class3 = int(input("Number of student in the third class"))

    if no_class1 % 2 == 1:    #for odd number of students
        desks1 = (no_class1 // 2) + 1
    else: #for even number of students
        desks1 = (no_class1 // 2)

    if no_class2 % 2 == 1:
        desks2 = (no_class2 // 2) + 1
    else:
        desks2 = (no_class2 // 2)

    if no_class3 % 2 == 1:
         desks3 = (no_class3 // 2) + 1
    else:
         desks3 = (no_class3 // 2)

    print(desks1 + desks2 + desks3)

#calling out the function
maths_calc()

