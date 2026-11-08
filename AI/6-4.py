n=int(input())
key=(input().split())
for i in range(n):
    for j in range(i+1,n):
        if key[i]+key[j]<key[j]+key[i]:
            key[i],key[j]=key[j],key[i]
result=''.join(key)
print(result)