import sys

data=sys.stdin.read()
length=len(data)
# print([s for s in data])
# print([data[i] for i in range(length)])

res=''
i=0
while i<length:
#     print(data[i])
    if data[i]=='"' and not (i > 0 and data[i-1] == '\\'):
        for j in range(i+1, length):
            if data[j]=='"' and (data[j-1]!='\\' or (data[j-1]=='\\' and data[j-2]=='\\')) :
                res+= data[i: j+1]
                i=j+1
                break
    elif data[i]=='/' and i+1<length and data[i+1]=='*':
        find=False
        for j in range(i+2, length-1):
            if data[j]=='*' and data[j+1]=='/':
                find=True
                i=j+2
                break
        
        if not find:
            res+=data[i:]
            break
    else:
        res+=data[i]
        i+=1

sys.stdout.write(res)