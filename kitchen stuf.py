# cook your dish here
n=int(input())
for i in range(n):
    c=int(input())
    s=[int(x) for x in input().split(' ')][:c]
    b=[int(x) for x in input().split(' ')][:c]
    c=0
    val=0
    for i in range(len(s)):
        val=s[i]-val
        if b[i]<=val:
            c+=1
        val=s[i]
    print(c)
