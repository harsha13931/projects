# cook your dish here
n = int(input())
for i in range(n):
    a, b, c, d, f = input().split()
    p = ((int(c) * int(f)) + int(a))
    d = ((int(d) * int(f)) + int(b))
    if p > d:
        print('DIESEL')
    elif p < d:
        print('PETROL')
    else:
        print('SAME PRICE')




