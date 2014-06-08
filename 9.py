#a^2 + b^2 = c^2
#a + b + c = 1000

from itertools import product

for a,b in product(range(1,1001),range(1,1001)):
    c = 1000 - (a+b)
    if a**2 + b**2 == c**2:
        print(a*b*c)
        break
else:
    print('failed')

