l=[x for x in input().split(' ')]
x=[]
print(len(l))
for i in l:
    print(i[0])
    if i[0]=='a' or i[0]=='A':
        x.append(i)
print(x)
