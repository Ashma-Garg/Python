#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    count=0
    pc=0
    zc=0
    n=len(arr)
    for i in range(n):
        if arr[i]<0:
            count=count+1
        elif arr[i]>0:
            pc=pc+1
        else:
            zc=zc+1
    print("{:.6f}".format(float(pc/n)))
    # Also this method can be approched for fixed decimal values
    # elif self.real == 0:
    #         if self.imaginary >= 0:
    #             result = "0.00+%.2fi" % (self.imaginary)
    print("{:.6f}".format(float(count/n)))
    print("{:.6f}".format(float(zc/n)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
