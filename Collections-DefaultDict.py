# # The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.
# # For example:
# #
# # from collections import defaultdict
# # d = defaultdict(list)
# # d['python'].append("awesome")
# # d['something-else'].append("not relevant")
# # d['python'].append("language")
# # for i in d.items():
# #     print i
# # This prints:
# #
# # ('python', ['awesome', 'language'])
# # ('something-else', ['not relevant'])
# Sample Input
#
# STDIN   Function
# -----   --------
# 5 2     group A size n = 5, group B size m = 2
# a       group A contains 'a', 'a', 'b', 'a', 'b'
# a
# b
# a
# b
# a       group B contains 'a', 'b'
# b
# Sample Output
#
# 1 2 4
# 3 5
# Explanation
#
# 'a' appeared  times in positions 1, 2 and 4.
# 'b' appeared  times in positions 3 and 5.
# In the sample problem, if 'c' also appeared in word group B, you would print -1.
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n,m=input().split()
ls=list()
d=defaultdict(list)
for i in range(int(n)):
    num=input()
    d[num].append(str(i+1))
for j in range(int(m)):
    o=input()
    if(d[o]):
        print(" ".join(d[o]))
    else:
        print("-1")
