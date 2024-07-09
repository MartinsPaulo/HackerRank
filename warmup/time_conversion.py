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

def timeConversion(s):
    time = s.split(':')
    hours = int(time[0])

    if ( time[2][-2:].upper() =="PM" and hours != 12) or (time[2][-2:].upper() == "AM" and hours >= 12):
        hours = hours+12
    
    hours_str = str(hours%24)
    
    return f"{ hours_str if len(hours_str) == 2 else '0' + hours_str}:{time[1]}:{time[2][:2]}"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
                                                                                                                                                                                                                                                                                                                                                                                                                                                   
