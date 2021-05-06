#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    # Write your code here
    count=0
    # could have used floor and ceil too to make it easy
    while(not str(math.sqrt(a)).endswith(".0")):
        a=a+1
    second=math.sqrt(a)
    first=second-1
    sqfirst=first*first
    diff=a-sqfirst
    while(a<=b):
        a=a+diff+2
        diff=diff+2
        count=count+1
    return count

    # This solution occurs timeout error
    # count=0
    # for i in range(a,b+1):
    #     if (str(math.sqrt(i)).endswith(".0")):
    #         count=count+1
    # return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
