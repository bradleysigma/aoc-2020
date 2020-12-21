import aoc
data = aoc.strlist(3)

p = len(data)
q = len(data[0])
n = "".join(i[j % q] for i, j in zip(data, range(0, 3 * p, 3))).count("#")

m = n
for u, v in [(1, 1), (5, 1), (7, 1), (1, 2)]:
    m *= "".join(i[j % q] for i, j in zip(data[::v], range(0, u * p // v, u))).count("#")

print(n, m)
aoc.tock("ms")
