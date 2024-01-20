n=int(input())
for i in range(n):
    l=[int(x) for x in input().split(' ')]
    s=sum(l)
    k=oct(s)
    print(k)
    s=str(k )
    if '1' in s:
        print('no')
    else:
        print(s[2:])
