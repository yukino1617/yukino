def printJinzita(T):
    a=ord('A')
    target=ord(T)
    count=0
    while count<=target-a:
        print(' '*(target-a-count),end="")
        for i in range(a,a+count+1):
            print(chr(i),end="")
        key=0
        while (a+count-key-1)>=a:
            print(chr(a+count-key-1),end="")
            key+=1
        print()
        count+=1
target=input()
printJinzita(target)

