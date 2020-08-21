import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
count=dict()
words=list()
state="Out"
wc=0
i=0
charac=""
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
    d=data.decode()
    for e in d:         # here e returns a single character because in mysock.recv(512)
                        #it meant 512 characters. It is not returning any line or string.
                        #So it we want count of words we'll have to combine characters and form words.
        if e==" " or e=="\n" or e=="\t":
            state="Out"
            count[charac]=count.get(charac,0)+1
            i=i+1
        elif state=="Out":
            state="In"
            charac=e
            wc=wc+1     #total words
        else:
            charac+=e
print(wc)
sorted(count)
for k,v in count.items():
    print("\" ",k,"\"","\t",v)
mysock.close()
