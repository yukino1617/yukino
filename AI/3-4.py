T = int(input())
for i in range(T):
    n = int(input())
    a = (n+1)//2
    for j in range(1,a+1):
        b = a - j
        c = 2 * j -1
        print(" "*b+"*"*c)
    for u in range(a -1,0,-1):
        b = a - u
        c = 2*u-1
        print(" "* b + "*" * c)
        