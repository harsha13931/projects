n=int(input())
for i in range(n):
    l=[int(x) for x in input().split(' ')]
    if l[0]==l[2] or l[1]==l[3]:
        print('YES')
    else:
        print('NO')