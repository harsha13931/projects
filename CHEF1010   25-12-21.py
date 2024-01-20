# cook your dish here
n = int(input())
for i in range(n):
    m = 0
    k = 0
    n = int(input())
    l = input()
    for i in l:
        #print(i)
        if i=='1':
            m+=1
        else:
            k+=1
    #print(k,m)
    if m == 0 or k == 0:
        print(0)
    elif m==k:
        print(m-1)
    elif m < k:
       print(m - 1)
    else:
        print(k - 1)


