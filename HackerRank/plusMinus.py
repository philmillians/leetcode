#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    length_arr = len(arr)
    positives=0
    negatives=0
    zeroes =0
    for i in range (length_arr):
        if arr[i] > 0:
            positives+=1
        elif arr[i] < 0:
            negatives+=1
        elif arr[i] == 0:
            zeroes+=1
    positives=positives/length_arr
    p="{0:.6f}". format(positives)
    print(p)
    negatives=negatives/length_arr
    n="{0:.6f}". format(negatives)
    print(n)
    zeroes=zeroes/length_arr
    z="{0:.6f}". format(zeroes)
    print(z)
    
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

