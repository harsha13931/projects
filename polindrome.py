n=int(input())
for i in range(n):
    c=int(input())
    l=[int(x) for x in input().split(' ')]
    count=0
    for i in l:
        if i%2!=0:    #to find the noof operations to be done to make a polindrome
            count+=1
    if count==0:
        print(0)
    else:
        print(count//2)
