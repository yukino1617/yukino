import copy
n,k=map(int,input().split())
day=[]
night=[]
sum=0
day=list((map(int,(input().split()))))
night=list((map(int,(input().split()))))
dif=copy.deepcopy(night)
for i in range(n):
    dif[i]=day[i]-night[i]

sum=0

dif.sort(reverse=True)
for i in dif[:k]:
    sum+=i
for i in night:
    sum+=i
print(sum)