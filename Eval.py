# Task
# You are given an expression in a line. Read that line as a string variable, such as var, and print the result using eval(var).
#
# NOTE: Python2 users, please import from __future__ import print_function.
#
# Constraint
# Input string is less than 100 characters.
#
# Sample Input
#
# print(2 + 3)
# Sample Output
#
# 5

# For Pyhton 2:

from __future__ import print_function
#for Pyhton 2 have to use this import statement and here it is raw_input() only.
#dont use input()
inputString=raw_input()
eval(inputString)

# For Python 3:
eval(input())
