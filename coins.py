# cook your dish here
n=int(input())
for i in range(n):

    a,b=map(int,input().split())
    if a==0 and b%2==0:
        print('YES')
    elif a==0 and b%2!=0:
        print('NO')
    elif (a+b*2)%2==0:
        print('YES')
    else:
        print('NO')