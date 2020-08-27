#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    count=0
    count1=0
    for i in range(len(apples)):
        if(apples[i]>=0):
            if (apples[i]+a)>=s and (apples[i]+a)<=t:
                #print(apples[i]+a)
                count=count+1
    for j in range(len(oranges)):
        if(oranges[j]<=0):
            if (oranges[j]+b)<=t and (oranges[j]+b)>=s:
                count1=count1+1
    print(count)
    print(count1)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
