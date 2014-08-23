
from time import clock
limit = 2000000
clock()
lst = []
for x in xrange(0,limit + 1):
    lst.append(1)
lst[1] = lst[0] = 0
for x in xrange(0,limit + 1):
    if lst[x] == 1:
        for y in xrange(2 * x, limit + 1, x):
            lst[y] = 0
Sum = 0
for i in lst:
    if i == 1:
        Sum += 1
print Sum
print clock()