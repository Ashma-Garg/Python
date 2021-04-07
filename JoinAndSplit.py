def split_and_join(line):
    s=str()
    s="-".join(line.split(" "))
    return s
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
