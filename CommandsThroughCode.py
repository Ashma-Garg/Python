# Input Format
#
# The first line contains an integer,n , denoting the number of commands.
# Each line i of the n subsequent lines contains one of the commands described above.
#
# Constraints
#
# The elements added to the list must be integers.
# Output Format
#
# For each command of type print, print the list on a new line.
#
# Sample Input 0
#
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
# Sample Output 0
#
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]
if __name__ == '__main__':
    N = int(input())
    l=list()
    for i in range(N):
        lst=input().split()
        command=lst[0]
        args=lst[1:]
        if(command!="print"):
            command="l." + command + "(" + ",".join(args) + ")"
        else:
            command=command + "(l)"
        eval(command)
