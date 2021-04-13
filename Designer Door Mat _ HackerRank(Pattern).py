# Sample Input
#
# 9 27
# Sample Output
#
# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ----------WELCOME----------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------

#First and Short method: Need to understand it
# n, m = map(int,input().split())
# pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
# print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
for i in reversed(range(int(int(n)/2)+1)):
    if i is not 0:
        string=str()
        for j in range(i*3):
            string=string+"-"
            strin=str()
        for k in range((int(int(n)/2)-i)*2+1):
            strin=strin+".|."
        strin=string+strin+string
        print(strin)
string=str()
for i in range(int(int(n)/2)*3-2):
    string=string+"-"
string=string+"WELCOME"+string
print(string)
for i in (range(1,int(int(n)/2)+1)):
    string=""
    if i is not 0:
        for j in range(i*3):
            string=string+"-"
            strin=str()
        for k in range((int(int(n)/2)-i)*2+1):
            strin=strin+".|."
        strin=string+strin+string
        print(strin)
