# cook your dish here
c = int(input())
for i in range(c):
    n = int(input())
    l = [int(x) for x in input().split(' ')]
    e = len(l)
    x = int((len(l) + 1) / 2)
    s = l[:(x - 1)]
    y = l[(x):]
    y = y[::-1]
    u = l[x - 1]
    q = len(y)
    z = len(s)
    w = l[x - 1]

    if (e % 2 != 0 and (l[-1] == 1 and l[0] == 1) and (q == (w - 1) and (z == (w - 1)))) or (
            u - 1 == len(y) and u + 1 == len(s)):
        print('yes')
    else:
        print('no')

