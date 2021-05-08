#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    # Write your code here
    j=0
    count=list()

    while(arr):
        print(arr)
        s=0
        d=list()
        minimum=min(arr)
        for i in range(0,len(arr)):
            if arr[i] > 0:
                s=s+1
                arr[i]=arr[i]-minimum
                if(arr[i]!=0):
                    d.append(arr[i])

        arr=d
        j=j+1
        count.append(s)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
