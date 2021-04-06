# Let's dive into the interesting topic of regular expressions! You are given some input, and you are required to check whether they are valid mobile numbers.
#
# A valid mobile number is a ten digit number starting with a 7, 8 or 9.
#
# Concept
#
# A valid mobile number is a ten digit number starting with a 7, 8 or 9.
#
# Regular expressions are a key concept in any programming language. A quick explanation with Python examples is available here. You could also go through the link below to read more about regular expressions in Python.
#
# https://developers.google.com/edu/python/regular-expressions

# Output Format
#
# For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines. Do not print the quotes.
#
# Sample Input
#
# 2
# 9587456281
# 1252478965
# Sample Output
#
# YES
# NO
# Enter your code here. Read input from STDIN. Print output to STDOUT

# First Solution
# import re
# [print('YES' if re.match(r'^[789]\d{9}$',input()) else 'NO') for _ in range(int(input()))]

# Socond solution
import re
for _ in range(int(input())):
    digit=input();
    if bool(re.match('^[7-9]\d+$',digit)) and len(digit)==10:
        print("YES")
    else:
        print("NO")
