# Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.
#
# Sample Input 0
#
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output 0
#
# Berry
# Harry

if __name__ == '__main__':

    lst=list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append([name,score])

    lst.sort(key=lambda x:x[1])
    first=lst[0][1]
    second=''
    for l in range(len(lst)):
        if(lst[l][1])!=first:
            second=lst[l][1]
            break
    lst=[lst[i][0] for i in range(len(lst)) if lst[i][1]==second]

    lst.sort()
    for l in lst:
        print(l)
