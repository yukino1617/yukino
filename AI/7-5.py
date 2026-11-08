a = list(map(int,input().split()))
  
def solve(a):
    ans = ''
    first = 0
    if sum(a) == 1:
        for i in range(10):
            if a[i]:
                print(i)
                return
    sp = -1
    cnt = 0
    for i in range(10):
        if a[i]%2:
            cnt+=1
            sp = i
            if cnt>1:
                print(-1)
                return
    if sum(a[1:]) == 1 and a[0]:
        print(-1)
        return
    od = False
    if cnt:
        od = True
    for i in range(1,10):
        if a[i]:
            ans+=str(i)
            a[i]-=2
            break
    ans+='0'*(a[0]//2)
    for i in range(1,10):
        ans+=str(i)*(a[i]//2)
    print(ans,end = '')
    if od:
        print(sp,end = '')
    print(ans[::-1])
solve(a)