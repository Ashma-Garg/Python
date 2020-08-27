#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i]<38:
            print(grades[i])
        elif grades[i]%5!=0 :
            x=int(grades[i]%5)
            x=5-x
            if x<3:
                grades[i]=grades[i]+x
    return grades
    # Write your code here

if __name__ == '__main__':
    n=input("Enter Size of List: ");
    lst=list()
    for i in range(int(n)):
        x=int(input())
        lst.append(x)
    result = gradingStudents(lst)

    for i in range(int(n)):
        print(lst[i])
