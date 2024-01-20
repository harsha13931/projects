n = int(input())
for i in range(n):
    a, b, c, d = map(int, input().split(' '))
    k = (a * d) / 100
    print(k)
    s = abs(a + k)
    print(s)
    if s >= b and s <= c:
        print('Yes')
    else:
        print('No')

