m = []
for i in range(10):
    l = [int(x) for x in input().split(' ')]
    m.append(l)
s = 0
for i in range(10):
    for j in range(10):
        print(m[i][j])
    s += m[i][i]

print(s)
