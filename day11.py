import aoc
data = aoc.strlist(11)

h = len(data)
w = len(data[0])
p = {}
q = {}
for i in range(w):
    for j in range(h):
        if data[j][i] == ".": continue
        p[i,j] = data[j][i]
        q[i,j] = data[j][i]

d = {}
for i in range(w):
    for j in range(h):
        d[i,j] = []
        for u,v in ((1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1)):
            if (i+u,j+v) in p:
                d[i,j].append((i+u,j+v))

c = set(p.keys())
while c:
    pp = dict(p)
    cc = set()
    for i,j in c:
        n = [p[k] for k in d[i,j]].count("#")
        if p[i,j] == "L" and n == 0:
            pp[i,j] = "#"
            cc.update(d[i,j])
        elif p[i,j] == "#" and n >= 4:
            pp[i,j] = "L"
            cc.update(d[i,j])
    p = pp
    c = cc

d = {}
for i in range(w):
    for j in range(h):
        d[i,j] = []
        for u,v in ((1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1)):
            r = 1
            while (0 <= i+r*u < w) and (0 <= j+r*v < h):
                if (i+r*u,j+r*v) in q:
                    d[i,j].append((i+r*u,j+r*v))
                    break
                r += 1

c = set(q.keys())
while c:
    qq = dict(q)
    cc = set()
    for i,j in c:
        n = [q[k] for k in d[i,j]].count("#")
        if q[i,j] == "L" and n == 0:
            qq[i,j] = "#"
            cc.update(d[i,j])
        elif q[i,j] == "#" and n >= 5:
            qq[i,j] = "L"
            cc.update(d[i,j])
    q = qq
    c = cc

print(list(p.values()).count("#"), list(q.values()).count("#"))

aoc.tock()
