import sys
import copy
a=int(input())
List=[]
ListA=[]
tmp=a
tmp1=a
count=0
while tmp1>0:
    tmp1//=10
    count+=1

while a>0:
    List.append(a%10)
    a//=10
ListA=copy.deepcopy(List)
ListA.reverse()
resultList=ListA+List[1::1]
result=0
for i in resultList:
    result=result*10+i
if result<=2:
    print("prime")
else :
    i=2
    while i*i<=result:
        if result%i==0:
            print("noprime")
            sys.exit()
        else :
            i+=1
            continue
print("prime")
sys.exit()