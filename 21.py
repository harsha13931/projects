# cook your dish here
n=int(input())
for i  in range(n):
    a,b=map(int,input().split(' '))
    if a==b or a>b:
        print('YES')
    else:
        print('NO')