a,b=map(int,input().split())
count=0
for i in range (a,b+1):
    sum=0
    while i>0:
        sum+=(i%10)
        i//=10
    if sum%5==0:
        count+=1
    else:
        continue
print(count)