ans = []
for i in range(10):
    for j in range(1000,10000):
        s=i*j
        a=str(s)+str(i)+str(j)
        if (len(a)!=9):
            continue
        if set(a)=={'1','2','3','4','5','6','7','8','9'}:
            small = min(i,j)
            big = max(i,j)
            ans.append((s,small,big))
for i in range (10,100):
    for j in range(100,1000):
        s=i*j
        a=str(s)+str(i)+str(j)
        if (len(a)!=9):
            continue
        if set(a)=={'1','2','3','4','5','6','7','8','9'}:
            small = min(i,j)
            big = max(i,j)
            ans.append((s,small,big))
ans = list(dict.fromkeys(ans))
ans.sort(key = lambda x:(x[0],x[1]))
for s,i,j in ans:
    print(f"{s} = {i} x {j}")