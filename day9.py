import aoc
data = aoc.intlist(9)

i = 25
while any(data[i] - data[j] in data[j:i] for j in range(i - 25, i)):
    i += 1
n = data[i]

i, j = 0, 0
m = 0
while m != n:
    while m < n:
        m += data[j]
        j += 1
    while m > n:
        m -= data[i]
        i += 1

print(n, max(data[i:j]) + min(data[i:j]))
aoc.tock("ms")
