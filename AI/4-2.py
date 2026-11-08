n,target=(map(int,input().split()))
List =[]
for i in range (1,n+1):
    while i>0:
        List.append(i%10)
        i//=10
print(List.count(target))