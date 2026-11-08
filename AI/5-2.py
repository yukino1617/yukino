import sys

for line in sys.stdin:
    lineemx=line.strip()
    if not lineemx:
        continue
    year,month,target=map(int,line.split())
    day=0
    list=[]
        
    if month in (1,3,5,7,8,10,12):
        day=31
    elif month in (4,6,11,9):
        day=30
    else:
        if (year%4==0 and year%100!=0 ) or (year % 400 == 0):
            day=29
        else :
            day=28
    emx=year
    listy=[]
    listm=[]
    while emx>0:
        listy.append(emx%10)
        emx//=10
    if month<10:
        listm.append(0)
        listm.append(month)
    else :
        listm.append(month//10)
        listm.append(month%10)
    for i in range (1,day+1):
        list+=listy
        list+=listm
        if i<10:
            list.append(0)
            list.append(i)
        else :
            list.append(i%10)
            list.append(i//10)
    print(list.count(target))