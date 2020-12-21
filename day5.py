import aoc
data = aoc.strlist(5)

y = set()
for i in data:
    y.add(int(i.translate("".maketrans("FBLR", "0101")), 2))
print(max(y), (set(range(min(y), max(y) + 1)) - y).pop())

aoc.tock("ms")
