n=int(input())
sum=0
while(n>0 or sum>9):
    if n==0:
        n=sum
        sum=0
    c=n%10
    sum=sum+c
    n=n//10
print(sum)





def dig(n):
    if n==0:
        return 0
    if n%9==0:
        return 9
    else:                      #2nd method
        return(n%9)
n=1345
print(dig(n))
