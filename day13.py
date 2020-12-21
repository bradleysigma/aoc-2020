import aoc

# def gcd(a, b): return abs(a + b) if a * b == 0 else gcd(b, a % b)
data = aoc.strlist(13)
t = int(data[0])
b = [int(i) for i in data[1].replace("x", "0").split(",")]
n, m = max(b), 0
d = 1
y = 100000000000000
for i, j in enumerate(b):
    if j == 0: continue
    for k in range(n):
        if (t + k) % j == 0:
            n, m = k, j
            break
    while (y + i) % j:
        y += d
    d *= j
    # d = (d * j) // gcd(d, j)
print(n * m, y)
aoc.tock("ms")
