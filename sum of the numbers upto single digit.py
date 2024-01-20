 #You are using Python
n=int(input())
l=[int(x) for x in input().split(' ')]
s=sum(l)
print(s)
i=s%9
if i==0:
    print(9)
else:
    print(i)
