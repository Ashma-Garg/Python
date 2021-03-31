# Input Format
#
# The first line contains an integer,n , denoting the number of elements in the tuple.
# The second line contains  space-separated integers describing the elements in tuple tn.
#
# Output Format
#
# Print the result of hash(t).
#
# Sample Input 0
#
# 2
# 1 2
# Sample Output 0
# 3713081631934410656

3713081631934410656
if __name__ == '__main__':
    n = int(input())
    integer_list = (map(int, input().split()))
    # remember hash of list and tuple is different
    print(hash(tuple(integer_list)))
