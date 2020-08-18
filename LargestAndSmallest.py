maximum = None
minimum = None
#decide=True
while True:
    num = input("Enter a number: ")
    if num =="done":
        break
    else:
        try:
            n=int(num)
        except:
            print("Invalid input")
            continue
        maximum=max(n,maximum)
        if minimum is None:
            minimum=n
        minimum=min(n,minimum)

print("Maximum is", maximum)
print("Minimum is", minimum)
