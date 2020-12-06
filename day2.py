import aoc

x = aoc.strlist(2)

n = 0
m = 0
for i in x:
    u, v, c, p = i.replace(": ", "-").replace(" ", "-").split("-")
    u, v = int(u), int(v)
    if u <= p.count(c) <= v:
        n += 1
    if (p[u-1] == c) != (p[v-1] == c):
        m += 1
print(n, m)

aoc.tock("ms")
