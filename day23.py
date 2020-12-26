import aoc
data = aoc.intlist(23, d="")
N, V = 1, 0

z = 9
c = [[1]]
r = [None, c[0]]
for i in range(1, z):
    c.append([i+1])
    r.append(c[-1])
    c[i-1].append(c[i])
c[-1].append(c[0])

for i, j in enumerate(data):
    c[i][V] = j
    r[j] = c[i]

p = c[V]
for i in range(100):
    m = p[N], p[N][N], p[N][N][N]
    p[N] = p[N][N][N][N]
    u = p[V] - 1 or z
    while u in [j[V] for j in m]:
        u = u - 1 or z
    m[-1][N] = r[u][N]
    r[u][N] = m[0]
    p = p[N]

p = r[1][N]
s = ""
while p[V] != 1:
    s += str(p[V])
    p = p[N]


z = 1000000
c = [[1]]
r = [None, c[0]]
for i in range(1, z):
    c.append([i+1])
    r.append(c[-1])
    c[i-1].append(c[i])
c[-1].append(c[0])

for i, j in enumerate(data):
    c[i][V] = j
    r[j] = c[i]

p = c[V]
for i in range(10000000):
    m = p[N], p[N][N], p[N][N][N]
    p[N] = p[N][N][N][N]
    u = p[V] - 1 or z
    while u in [j[V] for j in m]:
        u = u - 1 or z
    m[-1][N] = r[u][N]
    r[u][N] = m[0]
    p = p[N]

print(s, r[1][N][V] * r[1][N][N][V])
aoc.tock()
