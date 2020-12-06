import aoc
data = aoc.strgroups(6)

n = 0
m = 0
for i in data:
    s = set(i[0])
    t = set(i[0])
    for j in i[1:]:
        s |= set(j)
        t &= set(j)
    n += len(s)
    m += len(t)
print(n, m)

aoc.tock("ms")
