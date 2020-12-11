import aoc
from collections import defaultdict
data = aoc.intlist(10, set)

d = defaultdict(int, {0:1})
for i in sorted(data):
    d[i] = d[i-1] + d[i-2] + d[i-3]

print((lambda x: (x+1)*(len(data)-x))(sum(j+1 in data for j in data)),
      d[max(d.keys())])

aoc.tock("ms")

##import aoc
##data = {0} | aoc.intlist(10, set)
##
##d = {i: 0 for i in range(6)}
##p = max(data)
##while p > 0:
##    n = max({p-i for i in range(6)} - data)
##    d[p-n] += 1
##    p = n - 2
##print((lambda x: x * (len(data)-x))(sum(j+1 in data for j in data)),
##      2**d[3] * 4**d[4] * 7**d[5])
##
##aoc.tock("ms")
