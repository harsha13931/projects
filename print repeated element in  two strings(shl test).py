n=input()
j=input()
l=''
#k=' '
s=set(n)
k=set(j)
#print(s)
#print(k)
if (len(set(n))-len(set(j)))==1:
    for i in k:
        if i in s:
            #print(i)
            s.remove(i)
    for i in s:
        #print(1)
        print(i)
            #print(k)
 #           break
else:
    for i in n:
        if i in j:
            n=n.replace(i,'')
            j=j.replace(i,'')
            #print(n)
            #print(j)
        else:
            l+=i
    print(l)
