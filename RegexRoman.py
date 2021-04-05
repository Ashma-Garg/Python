# Input Format
#
# A single line of input containing a string of Roman characters.
#
# Output Format
#
# Output a single line containing True or False according to the instructions above.
#
# Constraints
#
# The number will be between 1 and 3999 (both included).
#
# Sample Input
#
# CDXXI
# Sample Output
#
# True

# I
# X
# L
# C
# M
# D
# import roman
# x=input()
# try:
#     if (roman.fromRoman(x)>0 and roman.fromRoman(x)<4000):
#         print("True")
#     else:
#         print("False")
# except:
#     print("False")

# Second Solution

# thousand = 'M{0,3}'
# hundred = '(C[MD]|D?C{0,3})'
# ten = '(X[CL]|L?X{0,3})'
# digit = '(I[VX]|V?I{0,3})'
# regex_pattern = r''+thousand + hundred+ten+digit +'$'
#
# import re
# print(str(bool(re.match(regex_pattern, input()))))
