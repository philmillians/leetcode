#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    length_arr = len(arr)
    i=arr.index(max(arr))
    j=arr.index(min(arr))
    maxSum=0
    minSum=0
    sum=0
    for k in range (length_arr):
      if k == j:
        k+=1
      else:
        maxSum+= arr[k]
    for k in range (length_arr):
      if k == i:
        k+=1
      else:
        minSum+= arr[k]
    print(minSum, maxSum)
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

