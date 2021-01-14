#!/usr/bin/env python

import time
import math
from matplotlib import pyplot as plt

valid = False
count = 0

while not valid:
    try:
        num = int(input("\nEnter an integer greater than 1: \n"))
        if num <= 1:
            print("\nThe integer must be greater than 1\n")
            continue
        else:
            valid = True
    except:
        print("\nThe input is not an integer, try again\n")

start = num
arr = [(int((math.log10(num)))) + 1]

start_time = time.time()

while num != 1:
    
    if num % 2 == 0:
        num = num//2
    else:
        num = 3*num + 1

    print(num)
    arr.append((int((math.log10(num)))) + 1)
    count += 1


print("\nThe program took %d steps to go from %d to 1\n" % (count, start))

print("\nThe program took %s seconds to execute" % (time.time() - start_time))

plt.plot(arr)
plt.xlabel("Step number")
plt.ylabel("Number of digits")
plt.show()
