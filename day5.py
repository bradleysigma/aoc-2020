import aoc
data = aoc.strlist(5)

y = []
for i in data:
    y.append(int(i.translate("".maketrans("FBLR", "0101")), 2))
print(max(y), (set(range(min(y), max(y)+1)) - set(y)).pop())

aoc.tock("ms")
