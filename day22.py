import aoc
data = aoc.strgroups(22)
x = list(map(int, data[0][1:]))
y = list(map(int, data[1][1:]))

while x and y:
    i = x.pop(0)
    j = y.pop(0)
    if i > j:
        x.append(i)
        x.append(j)
    else:
        y.append(j)
        y.append(i)

n = sum(i * j for i, j in enumerate(reversed(x + y), 1))

u = {0: list(map(int, data[0][1:]))}
v = {0: list(map(int, data[1][1:]))}
p = {0: set()}
q = {0: set()}
t = 0
b = None
while t >= 0:
    while u[t] and v[t]:
        if tuple(u[t]) in p[t] or tuple(v[t]) in q[t]:
            t -= 1
            b = True
            break

        p[t].add(tuple(u[t]))
        q[t].add(tuple(v[t]))
        i = u[t].pop(0)
        j = v[t].pop(0)
        if len(u[t]) >= i and len(v[t]) >= j:
            if b is None:
                u[t].insert(0, i)
                v[t].insert(0, j)
                p[t].remove(tuple(u[t]))
                q[t].remove(tuple(v[t]))
                t += 1
                u[t] = u[t-1][1:i+1]
                v[t] = v[t-1][1:j+1]
                p[t] = set()
                q[t] = set()
                break
            else:
                w = b
                b = None
        else:
            w = i > j

        if w:
            u[t].append(i)
            u[t].append(j)
        else:
            v[t].append(j)
            v[t].append(i)
    else:
        b = bool(u[t])
        t -= 1

m = sum(i * j for i, j in enumerate(reversed(u[0] + v[0]), 1))

print(n, m)
aoc.tock()
