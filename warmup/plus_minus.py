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
    a_l = len(arr)
    p = n = z = 0
    
    for a in arr:
        if a > 0:
            p +=1
        elif a < 0:
            n +=1
        else:
            z +=1
            
    print(f"{(p/a_l):.4f}" if p != 0 else "0.0000")
    print(f"{(n/a_l):.4f}" if n != 0 else "0.0000")
    print(f"{(z/a_l):.4f}" if z != 0 else "0.0000")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
