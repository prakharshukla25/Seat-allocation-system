#!/bin/python3

import os
import sys



def berthType(n):
    
    if n % 8 == 7:
        return "SLB"
    elif n % 8 == 0:
        return "SUB"
    elif n % 8 == 1 or n % 8 == 4:
        return "LB"
    elif n % 8 == 2 or n % 8 == 5:
        return "MB"
    else:
        return "UB"

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = berthType(n)

    f.write(result + '\n')

    f.close()
