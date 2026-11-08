n=int(input())
List=[]
List+=map(int,input().split())
ListUsable=[]
if n>15:
    ListUsable+=List[n-16:n:1]
else :
    ListUsable=List
last=ListUsable[-1]
if last==0:
    print("UP")
elif last==15:
    print("DOWN")
elif n==1:
    print(-1)
else:
    if ListUsable[-2]>last:
        print("DOWN")
    else :
        print("UP")