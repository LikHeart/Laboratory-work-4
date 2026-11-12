import sys
n = 1000
lst = list(range(n))
tpl = tuple(range(n))
st = set(range(n))
dct = {i: i for i in range(n)}
print(tpl)
print(st)
print(dct)
print(sys.getsizeof(dct))
