if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    arr=max(a)
    i=0;
    while max(a)==arr:
        a.remove(arr)

    print(max(a))
