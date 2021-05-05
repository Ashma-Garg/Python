# You have two strings of lowercase English letters. You can perform two types of operations on the first string:
#
# 1. Append a lowercase English letter to the end of the string.
2. # Delete the last character of the string. Performing this operation on an empty string results in an empty string.
# Given an integer, k, and two strings, s and t, determine whether or not you can convert s to t by performing exactly k of the above operations on . If it's possible, print Yes. Otherwise, print No.
#
# Example. s=[a,b,c]
# t=[d,e,f]
#
# To convert s to t, we first delete all of the characters in 3 moves. Next we add each of the characters of t in order. On the 6th move, you will have the matching string. Return Yes.
#
# If there were more moves available, they could have been eliminated by performing multiple deletions on an empty string. If there were fewer than 6 moves, we would not have succeeded in creating the new string.
# Sample Input 0
#
# hackerhappy
# hackerrank
# 9
# Sample Output 0
#
# Yes
# Explanation 0
#
# We perform 5 delete operations to reduce string s to hacker. Next, we perform 4 append operations (i.e., r, a, n, and k), to get hackerrank. Because we were able to convert s to t by performing exactly k=9 operations, we return Yes.
#
# Sample Input 1
#
# aba
# aba
# 7
# Sample Output 1
#
# Yes
# Explanation 1
#
# We perform 4 delete operations to reduce string s to the empty string. Recall that though the string will be empty after 3 deletions, we can still perform a delete operation on an empty string to get the empty string. Next, we perform 3 append operations (i.e., a, b, and a). Because we were able to convert s to t by performing exactly k=7 operations, we return Yes.
#
# Sample Input 2
#
# ashley
# ash
# 2
# Sample Output 2
#
# No
# Explanation 2
#
# To convert ashley to ash a minimum of 3 steps are needed. Hence we print No as answer.
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    L=len(s)+len(t)
    i=0
    while i<len(s) and i<len(t) and s[i]==t[i]:
        i=i+1
    if(L <= k + i*2 and L%2 == k%2 or L < k):
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
