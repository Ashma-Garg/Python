# Sample Input
#
# chris alan
# Sample Output
#
# Chris Alan

#!/bin/python3

import math
import os
import random
import re
import sys
import string
# Complete the solve function below.
def solve(s):
    for i in s.split():
        s=s.replace(i,i.capitalize())

    return s
    
    # Below methods will eliminate double spaces and replace double space with single space
    # l=list()
    # l=s.split()
    # return " ".join(i.capitalize() for i in s.split())
    # for i in range(len(l)):
    #     l[i]=l[i].capitalize()

    # return " ".join(l)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
