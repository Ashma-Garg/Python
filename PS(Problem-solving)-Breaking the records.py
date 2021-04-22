

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    minN=None
    maxN=None
    mincount=0
    maxcount=0
    for l in scores:
        if minN is None and maxN is None:
            minN=int(l)
            maxN=int(l)
        elif int(l)<minN:
            minN=int(l)
            mincount+=1
        elif int(l)>maxN:
            maxN=int(l)
            maxcount+=1
    return [maxcount,mincount]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
