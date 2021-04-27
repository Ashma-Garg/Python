# Given an array of integers and a positive integer k, determine the number of (i,j) pairs where i<j and  ar[i]+ar[j]  is divisible by k.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    count=0
    for i in range(n):
        for j in range(i+1,n):
            if((ar[i]+ar[j])%k==0):
                count+=1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
s
