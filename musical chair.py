# cook your dish here
n=int(input())
c=0
for i in range(n):
    g=int(input())
    for i in range(1,g):
        if (g-1)%i==0:
            c+=1
    print(c)