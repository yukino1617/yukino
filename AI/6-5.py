import sys
Target=list(input())
countA=0
key =True

if len(Target)%2!=0:
    key=False
for i in Target:
    if i=='a':
        countA+=1
    elif i=='b':
        countA-=1
        if countA<0:
            key=False
            break
    else :
        key=False 
        break 
if   Target[0]!='a':
    key=False
elif countA>0:
    key=False
if key:
    print("Good")
    exit()
else:
    print("Bad")
    exit()


