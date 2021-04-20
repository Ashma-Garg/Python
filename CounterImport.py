# collections.Counter()
# A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
#
# Sample Code
#
# >>> from collections import Counter
# >>>
# >>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# >>> print Counter(myList)
# Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
# >>>
# >>> print Counter(myList).items()
# [(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
# >>>
# >>> print Counter(myList).keys()
# [1, 2, 3, 4, 5]
# >>>
# >>> print Counter(myList).values()
# [3, 4, 4, 2, 1]
# Task
#
#Raghu  is a shoe shop owner. His shop has X number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are N number of customers who are willing to pay x amount of money only if they get the shoe of their desired size.
#
# Your task is to compute how much money Raghu earned.
#
# Input Format
#
# The first line contains X, the number of shoes.
# The second line contains the space separated list of all the shoe sizes in the shop.
# The third line contains N, the number of customers.
# The next N lines contain the space separated values of the shoe size desired by the customer and x, the price of the shoe.
#
# Output Format
#
# Print the amount of money earned by Raghu.
#
# Sample Input
#
# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50
# Sample Output
#
# 200

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
x=int(input())
mylist=list()

mylist=input().split(" ")
N=int(input())
lst=list()
for _ in range(N):
    lst.append(input().split())
d=dict()
d=Counter(mylist)
addition=0
for i in lst:
    if(d.get(i[0])):
        addition=addition+int(i[1])
        d[i[0]]=d.get(i[0])-1
    # print(i[0])
print(addition)
# print(Counter(**lst))
