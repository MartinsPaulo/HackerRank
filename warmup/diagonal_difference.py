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
    array_column = len(arr[0])
    
    array_dig_1 = 0
    array_dig_2 = 0
    
    for count in range(array_column):
        array_dig_1 = array_dig_1 + arr[count][count]
    
    for count in range(array_column):
        array_dig_2 = array_dig_2 + arr[count][(array_column-1)-count]
    
    return abs(array_dig_1 - array_dig_2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
