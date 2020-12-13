import aoc

##def gcd(a,b): return abs(a+b) if a*b == 0 else gcd(b, a%b)
data = aoc.read(13).strip("\n")
t = int(data.split("\n")[0])
b = list(map(int, [i for i in data.split("\n")[1].replace("x", "0").split(",")]))
n, m = max(b), 0
d = 1
y = 100000000000000
for i in range(len(b)):
    if b[i] == 0: continue
    for j in range(n):
        if (t+j)%b[i] == 0:
            n, m = j, b[i]
            break
    while y%b[i] != (-i)%b[i]:
        y += d
    d *= b[i]
##    d = (d * b[i]) // gcd(d, b[i])
print(n*m, y)
