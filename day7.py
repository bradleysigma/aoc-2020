import aoc
data = aoc.strlist(7)

from collections import deque

bags = {}
for i in data:
    outer, inner = i.rstrip(".").split(" contain ")
    outer = outer.rstrip("s")
    bags[outer] = []
    if inner == "no other bags":
        continue
    for j in inner.split(", "):
        n, col = j.split(" ", 1)
        col = col.rstrip("s")
        n = int(n)
        bags[outer].append((n, col))

contain = set()
queue = deque(["shiny gold bag"])
while queue:
    i = queue.pop()
    for outer, inner in bags.items():
        for j in inner:
            if j[1] == i:
                contain.add(outer)
                queue.append(outer)

queue = deque([(1, "shiny gold bag")])
count = 0
while queue:
    r, i = queue.pop()
    for j in bags[i]:
        count += r*j[0]
        queue.append((r*j[0], j[1]))

print(len(contain), count)
aoc.tock("ms")
