import sys
n=int(input())
A=list(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            tmp=[]
            tmp.append(A[i])
            tmp.append(A[j])
            tmp.append(A[k])
            tmp.sort()
            if tmp[0]+tmp[1]>tmp[2]:
                print(f"{tmp[0]} {tmp[1]} {tmp[2]}")
                exit()
print("No solution")
