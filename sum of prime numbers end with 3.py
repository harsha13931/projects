lower = 2
upper = int(input())
s=[]
c=0
for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           s.append(num)
print(s)
for i in s:
    if i%10==3 or i==3:
        c=c+i
print(c)

