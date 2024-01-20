# cook your dish here
n=int(input())
for i in range(n):
    a,b,c=map(int,input().split(' '))
    if a+b > c:
        print('TRAIN')
    elif a+b < c:
        print("PLANEBUS")
    else:
        print('EQUAL')