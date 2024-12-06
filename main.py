from itertools import *
n = 1
for i in product('АБВГДЕЖЗИК', repeat = 3):
    print(n, i)
    n += 1