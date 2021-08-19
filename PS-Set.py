# Input Format
#
# The first line of input contains an integer, M.
# The second line contains M space-separated integers.
# The third line contains an integer, N.
# The fourth line contains N space-separated integers.
#
# Output Format
#
# Output the symmetric difference integers in ascending order, one per line.
#
# Sample Input
#
# STDIN       Function
# -----       --------
# 4           set a size M = 4
# 2 4 5 9     a = {2, 4, 5, 9}
# 4           set b size N = 4
# 2 4 11 12   b = {2, 4, 11, 12}
# Sample Output
#
# 5
# 9
# 11
# 12


a=input()
l=list(map(int,input().split(' ')))
b=input()
l1=list(map(int,input().split(' ')))

l=set(l)
l1=set(l1)

l2=l.union(l1)
l3=l.intersection(l1)




p=sorted(list(l2.difference(l3)))
for i in p:
    print(i)
