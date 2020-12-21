import aoc
from collections import defaultdict
data = aoc.strlist(21)

d = {}
c = defaultdict(int)
for i in data:
    p, q = i.split(" (contains ")
    p = set(p.split(" "))
    q = q.rstrip(")").split(", ")
    for k in p:
        c[k] += 1
    for j in q:
        d[j] = d.get(j, p) & p

b = True
while b:
    b = any(len(i) > 1 for i in d.values())
    for i in filter(lambda k: len(d[k]) == 1, d):
        t, = d[i]
        c[t] = 0
        for j in filter(lambda k: t in d[k] and k != i, d):
            d[j].remove(t)

print(sum(c.values()), ",".join("".join(d[i]) for i in sorted(d)))
aoc.tock("ms")
