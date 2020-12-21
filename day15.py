import aoc
data = aoc.intlist(15, d=",")

d = {i: j for j, i in enumerate(data[:-1])}
p = data[-1]

for i in range(len(data), 2020):
    if p in d.keys():
        d[p], p = i - 1, i - d[p] - 1
    else:
        d[p], p = i - 1, 0

y = p

for i in range(2020, 30000000):
    if p in d.keys():
        d[p], p = i - 1, i - d[p] - 1
    else:
        d[p], p = i - 1, 0

print(y, p)
aoc.tock()
