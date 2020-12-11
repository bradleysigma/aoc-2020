import aoc
data = aoc.strgroups(6)

print(sum(len(set("".join(i))) for i in data),
      sum(len(set.intersection(*map(set, i))) for i in data))

aoc.tock("ms")
