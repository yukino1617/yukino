import sys
for line in sys.stdin:
    n=int(line.strip())
    for i in range(0,n+1):
        space=2*(n-i)
        stars=i+1
        print(" "*space+"*"*stars)
    for i in range(n-1,-1,-1):
        space=2*(n-i)
        stars=i+1
        print(" "*space+"*"*stars)