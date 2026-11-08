n,num=map(int,input().split())
n+=1
List=[]
for i in range (num):
    a,b=map(int,input().split())
    List+=range(a,b+1)
tmp=set(List)
result=list(tmp)
print(n-len(result))