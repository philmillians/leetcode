#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    counter1 = 0
    counter2 = (len(arr)-1)
    rt_arr = []
    lf_arr = []
    for i in range(len(arr)):
      lf_arr.append(arr[counter1][counter1])
      counter1 +=1
    counter1 = 0
    for i in range(len(arr)):
      rt_arr.append((arr[counter1][counter2]))
      counter1 +=1
      counter2 -=1
    return (abs(sum(lf_arr) - sum(rt_arr)))
      
      
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

