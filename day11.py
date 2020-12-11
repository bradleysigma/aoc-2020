import aoc
from collections import defaultdict
data = aoc.strlist(11)

h = len(data)
w = len(data[0])
p = defaultdict(lambda: ".")
q = defaultdict(lambda: ".")
for i in range(w):
    for j in range(h):
        p[(i,j)] = data[j][i]
        q[(i,j)] = data[j][i]

while True:
    pp = defaultdict(lambda: ".")
    for i in range(w):
        for j in range(h):
            n = [p[(i+u,j+v)] for u,v in ((1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1))].count("#")
            if p[(i,j)] == "L" and n == 0:
                pp[(i,j)] = "#"
            elif p[(i,j)] == "#" and n >= 4:
                pp[(i,j)] = "L"
            else:
                pp[(i,j)] = p[(i,j)]
    if all(p[k] == pp[k] for k in p.keys()): break
    p = pp

while True:
    qq = defaultdict(lambda: ".")
    for i in range(w):
        for j in range(h):
            if q[(i,j)] == ".": continue
            n = 0
            for u,v in ((1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1)):
                k = 1
                while (0 <= i+k*u < w) and (0 <= j+k*v < h):
                    if q[(i+k*u,j+k*v)] != ".":
                        n += int(q[(i+k*u,j+k*v)] == "#")
                        break
                    k += 1
            if q[(i,j)] == "L" and n == 0:
                qq[(i,j)] = "#"
            elif q[(i,j)] == "#" and n >= 5:
                qq[(i,j)] = "L"
            else:
                qq[(i,j)] = q[(i,j)]
    if all(q[k] == qq[k] for k in q.keys()): break
    q = qq

print(list(p.values()).count("#"), list(q.values()).count("#"))

aoc.tock()
