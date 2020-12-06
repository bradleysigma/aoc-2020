import aoc
data = aoc.strlist(3)

def path(geo, u, v):
    n = 0
    j = 0
    d = len(geo[0])
    for i in geo[::v]:
        if i[j%d] == "#":
            n += 1
        j += u
    return n

n = path(data, 3, 1)
print(n)
for x, y in [(1,1), (5,1), (7,1), (1,2)]:
    n *= path(data, x, y)
print(n)

aoc.tock("ms")
