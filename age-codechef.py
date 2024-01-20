from typing import List

digits=[9]
s = digits[-1]
if  s< 9:
    digits[-1] = s + 1
    print(digits)

else:
    digits[-1]=1
    print(digits)
    digits.append(0)
    print(digits)


