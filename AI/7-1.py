n,t=map(int,input().split())
a=input()
spot=-1
count=0
if '.' in a:
    pi,pf=a.split('.')
    pi=int(pi)
    key =False

    for i in a:
        if i=='.':
            spot=count
            break
        count+=1
    while t>0 and not key:
        key=True
        if len(pf)>0:
            for i in range (len(pf)):
                if pf[0]>='5':
                    pi+=1
                    pf=""
                    break
                elif  pf[i]>='5':
                    pf=str(int(pf[:i])+1)
                    key=False
                    break
        else :
            pf=""
            break
        t-=1

    
    partzhen=str(pi)
    result=''
    flag=False
    for i in pf:
        if i=='0':
            continue
        else :
            flag=True
    if flag:
        result=partzhen+'.'+pf
    else :
        result=partzhen
    print(result)
else :
    print(a)

