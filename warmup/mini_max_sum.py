#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def min_array(arr):
    aux = 10_000_000_000
    for a in arr:
        if a < aux:
            aux = a
    return aux
    
def max_array(arr):
    aux = 1
    for a in arr:
        if a > aux:
            aux = a
    return aux
    
def miniMaxSum(arr):
    l = []
    
    for a in arr:
        l.append(0)
    
    for c in range(len(arr)):
        for count in range(len(arr)): 
            if c != count:
                l[c] += arr[count]
                
    print(f"{min_array(l)} {max_array(l)}")


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
