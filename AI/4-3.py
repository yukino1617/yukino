n,k,m=map(int,input().split())
List=[]
for i in range (0,n):
    List.append(i)

out=(k+m-1)%n
while n>1:
    del List[out]
    n-=1
    out=(out+m-1)%n
print(List[0])
    