# Lilah has a string, s, of lowercase English letters that she repeated infinitely many times.
# Given an integer, n, find and print the number of letter a's in the first  letters of Lilah's infinite string.
# For example, if the string s="abcac" and n=10 , the substring we consider is abcacabcac, the first 10  characters of her infinite string. There are 4 occurrences of a in the substring.

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    num=len(s)
    d=dict()
    res=int(n/num)
    rem=n%num
    count=0
    for letter in s:
        if letter is 'a':
            count=count+1
    res=res*count
    count=0
    for i in range(rem):
        if s[i] is 'a':
            count=count+1
    res=res+count
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
