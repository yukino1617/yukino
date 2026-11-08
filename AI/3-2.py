n=int(input())
count=0
a=1
for i in range (1,n+1):
    for count in range(1,i+1):
        print(f"{a:4}",end="")
        a+=1
    print()
