import aoc
data = aoc.strgroups(20)

n = 1
for i in data:
    e = [i[1], i[-1], "".join(t[0] for t in i[1:]), "".join(t[-1] for t in i[1:])]
    for j in data:
        for k in [j[1], j[-1], "".join(t[0] for t in j[1:]), "".join(t[-1] for t in j[1:])]:
            if k in e:
                e.remove(k)
                break
            if k[::-1] in e:
                e.remove(k[::-1])
                break
    if len(e) == 2:
        n *= int(i[0].split(" ")[1].rstrip(":"))

q = sum(sum(j[1:-1].count("#") for j in i[2:-1]) for i in data)

# print(n, q - 15 * 32)
# print(n, q - 15 * 33)
# print(n, q - 15 * 34)
# print(n, q - 15 * 35)
# print(n, q - 15 * 36)
print(n, q - 15 * 37)

aoc.tock("ms")
