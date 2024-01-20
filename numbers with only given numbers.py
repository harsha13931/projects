s=int(input())
n=int(input())
l=['0','2','3','5','6','7','8']
c=0
for i in range(s,n):
    i=str(i)
    if any(x in i for x in l):
        #print(i)
        pass
    else:
        print(i)
        c+=1
print(c)
