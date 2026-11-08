T=int(input())
for i in range(T):
    n=int(input())
    ListA=list(map(int,input().split()))
    maxLi=max(ListA)
    minLi=min(ListA)
    sub=maxLi-minLi
    sum=0
    for i in ListA:
        sum+=i
    avg=sum/n
    fangcha=0.0
    for i in ListA:
        fangcha+=(i-avg)**2/n
    print(sub,end=" ")
    print(f"{fangcha:.3f}")