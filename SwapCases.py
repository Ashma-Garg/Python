# Sample Input 0
#
# HackerRank.com presents "Pythonist 2".
# Sample Output 0
#
# hACKERrANK.COM PRESENTS "pYTHONIST 2".

def swap_case(s):
    string=str()
    for i in s:
        if i>='a' and i<='z':
            string=string + str(chr(ord(i)-32))
        elif i>='A' and i<='Z':
            string=string + str(chr(ord(i)+32))
        else:
            string=string + i
    return string

# Method Second: Use BuildIn Method
    # return s.swapcase()

#Third Method: USe isupper() and islower()
    # st=str()
    # for i in s:
    #     if i.isupper():
    #         st=st + i.lower()
    #     else:
    #         st=st + i.upper()
    # return st;

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
