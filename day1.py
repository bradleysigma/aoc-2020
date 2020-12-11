import aoc

data = aoc.intlist(1, set)
n = 0
m = 0
for i in data:
    if 2020-i in data:
        n = i*(2020-i)
    for j in ([] if m else data):
        if 2020-i-j in data:
            m = i*j*(2020-i-j)
            break
    if n and m: break
print(n, m)

aoc.tock("ms")
