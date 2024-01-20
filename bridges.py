n = int(input())
for i in range(n):
    n, m = map(int, input().split(" "))
    s = []
    for i in range(1, n + 1):
        s.append(i)
    c = 0
    if m == n - 1:
        for i in range(m):
            print(s[i], s[i + 1])
    else:
        for i in range(m - 1):
            print(s[i], s[i + 1])
            c += 1
        if c < m:
            s.remove(s[1])

        for i in range(len(s)):
            print(s[i], s[i + 1])
            c += 1
            if c == m:
                break
            else:
                continue
