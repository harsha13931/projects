n = int(input())


def ladu(l):
    if x > 2:
        for i in range(len(l) - 1):
            d = l[i] + l[i + 1]
            print(d)
            s.append(d)
            x = len(s)
            if len(s) > 2:
                ladu(s)
            else:
                h = abs(s[0] - s[1])
                if h <= 1:
                    print('YES')
                else:
                    print('NO')


for i in range(n):
    c = int(input())
    x = 2 ** c

    l = [int(x) for x in input().split(' ')]
    s = []
    if x == 1:
        print('YES')
    elif x == 2:
        h = abs(l[0] - l[1])
        if h <= 1:
            print('YES')
        else:
            print('NO')
    else:
        ladu(l)

