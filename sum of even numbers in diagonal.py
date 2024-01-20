# You are using Python
n=int(input())
s=[]
for i in  range(n):
    l=[int(x) for x in input().split(' ')]
    s.append(l)
k=0
for i in range(1,n):
    if (s[i][i])%2==0:
        k+=s[i][i]
    else:
        pass
print(k)