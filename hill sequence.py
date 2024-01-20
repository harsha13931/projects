n=int(input())
for i in range(n):
    c=int(input())
    l=[int(x) for x in input().split(' ')]
    s=max(l)
    se=set(l)
    k=[]
    d=[]
    for i in se:
        l.remove(i)
    le=set(l)
    for i in le:
        l.remove(i)
    #print(l)
    if s in l or len(l)>0:
        print(-1)
    else:
        for i in se:
            k.append(i)
        k.sort(reverse=True)
        for i in le:
            d.append(i)
        d.sort()
        hill=d+k
        for i in hill:
            print(i,end=" ")
        print()
