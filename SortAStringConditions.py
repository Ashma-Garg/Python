# Enter your code here. Read input from STDIN. Print output to STDOUT

#big solution
# string=input()
# s=list()
# c=list()
# o=list()
# e=list()
# for i in range(len(string)):

#     if(string[i]>='a' and string[i]<='z'):
#        s.append(string[i])
#     elif(string[i]>='A' and string[i]<='Z'):
#         c.append(string[i])
#     elif(int(string[i])%2!=0):
#         o.append(string[i])
#     else:
#         e.append(string[i])

# s.sort()
# c.sort()
# o.sort()
# e.sort()
# st=str()
# for i in s:
#     st=st+i
# for j in c:
#     st=st+j
# for k in o:
#     st=st+k
# for l in e:
#     st=st+l
# print(st)

#short Solution:
print(*(sorted(input(), key=lambda x: (x.isdigit(), x.isdigit() and int(x)%2==0, x.isupper(), x.islower(), x))), sep='')
# I'm pretty sure I've figured it out.. here is each part in key explained-
# `
#
# 1. if isdigit, give higher priority. so alphas come before digits now
# Ex- Sorting1234 => Sorting1234
# 2. if isevendigit, give higher priority. so, among the digits, now even have higher priority. While the 1st part in key is maintained
# Ex- Sorting1234 => Sorting1324
# 3. next priority goes to upper case keeping both previous keys maintained. so uppercase can't go after the numbers as that key has higher priority.
# Ex - Sorting1234 => ortingS1324
# 4. next priority is given to lowercase characters, but that isn't required as it's the only ones left in alphanumeric characters. We will get the same output either way
# Ex - Sorting1234 => ortingS1324
# 5. now sort according to the characters, but keeping all the previous keys in mind, all the characters will be sorted in place, keeping their order as defined in previous keys
# Ex - Sorting1234 => ginortS1324
