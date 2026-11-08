import sys
a=[]
mid={
    (1,3):2,(3,1):2,(4,6):5,(6,4):5,(7,9):8,(9,7):8,
    (1,7):4,(7,1):4,(2,8):5,(8,2):5,(3,9):6,(9,3):6,
    (1,9):5,(9,1):5,(3,7):5,(7,3):5
}
for line in sys.stdin:
    line=line.strip()
    if not line:
        break
    a.append(list(map(int,line)))
for i in range(len(a)):
    flag=True
    tmp=set(a[i])
    if len(tmp)!=len(a[i]) or len(a[i])>9:
        flag=False
    else:
        for k in range(len(a[i])-1):
            if (a[i][k],a[i][k+1]) in mid:
                value=mid.get((a[i][k],a[i][k+1]))
                for j in range(k+1):
                    if a[i][j]==value:
                        break
                else:
                    flag=False
                    break
    if flag:
        print("YES")
    else :
        print("NO")
        

