# cook your dish here
c=0
n=int(input())
for i in range(n):
       s=int(input())
       l=[int(x) for x in input().split(' ')]
       j=[int(x) for x in input().split(' ')]
       for i in range(1,len(l)):
           l[i]=l[i]-l[i-1]
           l.append(l[i])
       print(l)