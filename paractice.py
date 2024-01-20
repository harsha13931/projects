s=int(input())
for i in range(s):
    for j in range(i,s):
        print(" ",end="")

    for j in range(i+1):
        print("3",end="")
    print()