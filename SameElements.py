
# Karl has an array of integers. He wants to reduce the array until all remaining elements are equal. Determine the minimum number of elements to delete to reach his goal.
# For example, if his array isarr=[1,2,2,3] , we see that he can delete the 2 elements 1 and 3 leaving arr=[2,2]. He could also delete both twos and either the 1 or the 3, but that would take 3 deletions. The minimum number of deletions is 2.
import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    d=dict()
    l=list()
    count=0
    c=0
    for a in arr:
        d[a]=d.get(a,0)+1

    m=(max(d.values()))
    count=len(arr)-m
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
