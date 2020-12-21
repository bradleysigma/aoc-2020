import aoc
from itertools import product

data = aoc.strlist(17)
x = set()
y = set()
for j in range(len(data)):
    for i in range(len(data[j])):
        if data[j][i] == "#":
            x.add((i, j, 0))
            y.add((i, j, 0, 0))

for c in range(6):
    xx = set()
    yy = set()
    v = (min(u[0] for u in x | y) - 1, max(u[0] for u in x | y) + 1,
         min(u[1] for u in x | y) - 1, max(u[1] for u in x | y) + 1,
         min(u[2] for u in x | y) - 1, max(u[2] for u in x | y) + 1,
         min(u[3] for u in y) - 1, max(u[3] for u in y) + 1,)
    for i in range(v[0], v[1] + 1):
        for j in range(v[2], v[3] + 1):
            for k in range(v[4], v[5] + 1):
                n = sum((i + p, j + q, k + r) in x for p, q, r in product((-1, 0, 1), repeat=3))
                n -= 1 if (i, j, k) in x else 0
                if n == 3 or (n == 2 and (i, j, k) in x):
                    xx.add((i, j, k))
                for h in range(v[6], v[7] + 1):
                    m = sum((i + p, j + q, k + r, h + t) in y for p, q, r, t in product((-1, 0, 1), repeat=4))
                    m -= 1 if (i, j, k, h) in y else 0
                    if m == 3 or (m == 2 and (i, j, k, h) in y):
                        yy.add((i, j, k, h))
    x = xx
    y = yy

print(len(x), len(y))
aoc.tock()
