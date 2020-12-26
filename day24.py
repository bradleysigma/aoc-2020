import aoc
from aoc import vec
data = aoc.strlist(24)

p = set()
h = {"w": vec((-1, 1, 0)), "e": vec((1, -1, 0)),
     "nw": vec((0, 1, -1)), "se": vec((0, -1, 1)),
     "sw": vec((-1, 0, 1)), "ne": vec((1, 0, -1))}

for i in data:
    x = vec.zero(3)
    j = 0
    while j < len(i):
        d = i[j:j+1] if i[j] in "we" else i[j:j+2]
        x += h[d]
        j += len(d)
    p ^= {x}
t = len(p)

for i in range(100):
    q = set()
    u = p | {j + d for d in h.values() for j in p}
    for j in u:
        n = sum(j + d in p for d in h.values())
        if n == 2 or (n == 1 and j in p):
            q.add(j)
    p = q

print(t, len(p))
aoc.tock()

# import aoc
# data = aoc.strlist(24)
#
# d = {("nw", "sw"): "w",
#      ("ne", "se"): "e",
#      ("ne", "w"): "nw",
#      ("nw", "e"): "ne",
#      ("se", "w"): "sw",
#      ("sw", "e"): "se",
#      ("e", "w"): "",
#      ("ne", "sw"): "",
#      ("se", "nw"): ""}
#
# p = set()
# for i in map(lambda x: x.replace("e", "e ").replace("w", "w ").split(" "), data):
#     while any(all(k in i for k in j) for j in d):
#         for j in d:
#             while all(k in i for k in j):
#                 for k in j:
#                     i.remove(k)
#                 i.append(d[j])
#     p ^= {tuple(sorted(filter(None, i)))}
# print(len(p))
