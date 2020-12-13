import aoc
from aoc import vec
data = aoc.strlist(12)

d = 0
x = vec([0,0])
y = vec([0,0])
p = vec([10,1])
m = {"N": vec([0, 1]), "S": vec([0, -1]), "W": vec([-1, 0]), "E": vec([1, 0])}

for i in data:
    c, n = i[0], int(i[1:])
    if c in "LR":
        n = (360-n if c == "L" else n) % 360
        for j in range(n//90):
            p = p.cross()
            d += 1
    elif c == "F":
        x += m["ESWN"[d%4]]*n
        y += n * p
    else:
        x += n * m[c]
        p += n * m[c]

print(x.manhattan(), y.manhattan())
aoc.tock("ms")
