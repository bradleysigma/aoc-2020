import aoc
data = aoc.strgroups(16)

criteria = data[0]
ticket = list(map(int, data[1][1].split(",")))
others = [list(map(int, i.split(","))) for i in data[2][1:]]
rules = {}

for i in criteria:
    name, cond = i.split(": ")
    rules[name] = (lambda a, b, c, d: lambda x: a <= x <= b or c <= x <= d)(*map(int, cond.replace(" or ", "-").split("-")))

n = 0
correct = []
for i in others:
    for j in i:
        if not any(k(j) for k in rules.values()):
            n += j
            break
    else:
        correct.append(i)

fields = [dict(rules) for i in range(len(rules))]
for i in range(len(fields)):
    for j in list(fields[i].keys()):
        if not all(fields[i][j](k[i]) for k in correct):
            del fields[i][j]

while any(len(k) > 1 for k in fields):
    for i in range(len(fields)):
        if len(fields[i]) != 1: continue
        k, = fields[i].keys()
        for j in range(len(fields)):
            if i == j: continue
            if k in fields[j]:
                del fields[j][k]

m = 1
for i, j in zip(ticket, (min(k.keys()) for k in fields)):
    if j.startswith("departure"):
        m *= i

print(n, m)
aoc.tock("ms")
