# cook your dish here
n=int(input())
for i in range(n):
    c=int(input())
    l=[int(x) for x in input().split(' ')]
    a1=max(l)
    a2=min(l)
    l.remove(max(l))
    a3=max(l)
    o=(a1-a2)*a3
    print(o)