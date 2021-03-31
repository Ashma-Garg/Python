# >>> all(['a'<'b','b'<'c'])
# True
# >>> all(['a'<'b','c'<'b'])
# False
# Enter your code here. Read input from STDIN. Print output to STDOUT

n=input()

lst=input().strip().split()
#[j=j[::-1]] is to reverse it
#all will check if each and every condition is true
#any will return true even if any one conditon is true and all other are false
print(all([int(i)>0 for i in lst]) and any([j==j[::-1] for j in lst]))
