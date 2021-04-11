# Sample Input 0
#
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Sample Output 0
#
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

import textwrap

def wrap(string, max_width):
    c=len(string)
    i=0
    arr=list()
    while(i<=c):
        arr.append(string[i:i+max_width])
        i=i+max_width
    s='\n'.join(arr)
    return s
#second Solution by Inbuild function
# return "\n".join(textwrap.wrap(string, max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
