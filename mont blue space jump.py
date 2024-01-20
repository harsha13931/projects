n = int(input())
c = 0
s = 0
l = [int(x) for x in input().split(' ')]
for i in range(0, len(l)):
    # print(i)
    # print(l[i+2])
    # print(len(l)-1)
    # if l[i]==1:
    #   s+=2
    #  c+=1
    # continue

    if s + 1 == len(l) - 1 or s + 1 == len(l) - 2:
        c += 1
        break
    elif l[s + 2] == 0:
        s = s + 2
        c += 1
        # continue
    elif l[s + 1] == 0 and l[s + 2] == 1:
        s = s + 1
        c += 1
        # continue
    # print(s)
print(c)
