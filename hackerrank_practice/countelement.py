# Count element greater than previous average
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#

def countResponseTimeRegressions(responseTimes):
    # Write your code here
    left = 0
    right = 1
    count = 0
    while right <= len(responseTimes)-1:
        temp = left
        s = 0
        average = 0
        for temp in range(right):
            print(f"right is {right}")
            print(responseTimes[temp])
            s = s+ responseTimes[temp]
        average = s/right 
        for temp in range(right):
            if responseTimes[temp] > average:
                count +=1
        right = right +1
    return count

if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)
