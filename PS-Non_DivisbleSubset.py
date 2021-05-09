#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    d=dict()
    for i in range(len(s)):
        rem=s[i]%k
        d[rem]=d.get(rem,0)+1
    count=0
    print(d)
    try:
        l=(list(d))
        print(l)
        for i in range(len(l)):
            print(l[i])
            print(d)
            for j in range(i+1,len(l)):
                if(l[j]+l[i]==k):
                    if(d[l[i]]>d[l[j]]):
                        d.pop(l[j])
                    else:
                        d.pop(l[i])
                        # i=i-1
        print(d)
        for key, value in d.items():
            count=count+value
            
                        
        # for key, value in d.items():
        #     for ke,v in d.items():
        #         if (key!=ke and key+ke== k):
        #             if(value>v):
        #                 d.pop(ke)
        #                 count=count+value
        #                 break
        #             else:
        #                 d.pop(key)
        #                 count=count+v
        #                 break
    except:
        pass
                        
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
