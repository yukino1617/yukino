T=int(input())

di={'zero':'0','two':'2','four':'4','six':'6','nine':'9'}

for i in range(T):
    s=input()
    for j,value in di.items():
        s=s.replace(j,value)
    kk=''
    for k in s:
        if k in di.values():
            kk+=k
    print(kk)
            