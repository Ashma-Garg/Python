# You are given a spreadsheet that contains a list of N athletes and their details (such as age, height, weight and so on). You are required to sort the data based on the Kth attribute and print the final resulting table. Follow the example given below for better understanding.
# Note that K is indexed from ) to M-1, where  is the number of attributes.
# Note: If two attributes are the same for different rows, for example, if two atheletes are of the same age, print the row that appeared first in the input.
# Input Format
# The first line contains N and M separated by a space.
# The next N lines each contain M elements.
# The last line contains K.
# Output Format
# Print the N lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.
# Sample Input 0
#
# 5 3
# 10 2 5
# 7 1 0
# 9 9 9
# 1 23 12
# 6 5 9
# 1
# Sample Output 0
#
# 7 1 0
# 10 2 5
# 6 5 9
# 9 9 9
# 1 23 12
# Explanation 0
#
# The details are sorted based on the second attribute, since K is zero-indexed.


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    lst=sorted(arr,key=lambda x:int(x[k]))

    for l in lst:
        #here print statement means print(*l,sep=' ') that means seperate the output by space. and Pointer l means ever element of l i.e. l[i]
        #here for ex lst=[[7,1,0],[10,3,4],[3,7,9]]
        #than output will be
        #7 1 0
        #10 3 4
        #3 7 9
        #if print state would be print(l,sep='/ ') then result would be
        #[7,1,0]/
        #[10,3,4]/
        #[3,7,9]/
        print(*l)
