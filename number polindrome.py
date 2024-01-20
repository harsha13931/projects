def palindrome(a):
    if a == reverse(a):
        return True
    else:
        return False


def reverse(x):
    rev = 0

    while (x > 0):
        a = x % 10
        rev = rev * 10 + a
        x = x // 10
    return rev


n = int(input())
if palindrome(n):
    print("Given number is already palindrome")
    print(n, "is a palindrome")
else:
    while palindrome(n) == False:
        a = n
        s = n + reverse(n)
        n = n + reverse(n)
        print(a, "+", s, "=", n)
    print(n, "is a palindrome")



# method 2
n = input()
c = n[::-1]


def reverse(x):
    rev = 0

    while (x > 0):
        a = x % 10
        rev = rev * 10 + a
        x = x // 10
    return rev


if n == c:
    print(n)

else:
    while n != c:
        a = n
        k = int(c)
        n = int(n) + int(c)
        print(a, '+', k, '=', n)

        if n == reverse(n):

            break
        else:
            continue
    print(n)
