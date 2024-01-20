l=[5,3,4,1,2]
d=[]
n=int(input())
for i in range(n):
    x=min(l)
    d.append(x)     #sort upto required number of times
    l.remove(x)
l1=d+l
for i in l1:
    print(i,end=" ")
