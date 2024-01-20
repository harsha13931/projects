n = int(input())
for i in range(n):
    n, m = map(int, input().split(" "))
    s = []
    for i in range(1, n + 1):
        s.append(i)
    l = s.copy()
    c = 0
    if m == n - 1:
        for i in range(m):
            print(s[i], s[i + 1])
    else:                              #it will give out put as   1 2 ,2 3,3 4,1 3,1 4,2 4
        for i in range(n - 1):
            print(s[i], s[i + 1])
            c += 1
        for i in range(m - 1):

            for j in range(i + 2, len(l)):
                print(s[i], l[j])
                c += 1
                if c == m:
                    break
                else:
                    continue
            break
