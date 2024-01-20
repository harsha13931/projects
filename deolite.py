n=[x for x in input().split(' ')]
e=""
s=False
for i in n:
    e+=i
a,b=map(int,input().split(' '))
c,d=map(int,input().split(' '))
s=set(e)
#c=0
#
l=[]
#for i in s:
 #   for j in e:
  #      if i==j:
   #         c+=1
    #l.append(c)
   # c=0
#print(l)
i=len(n)
if i<a or i>b:
    #print('No Output')
    s=True
        #break
if s==True:
    print('No Output')
else:
    for i in n:
        if (len(i)>=c and len(i)<=d) and (len(i)>= int(b/2)):
            print(i,end=' ')
