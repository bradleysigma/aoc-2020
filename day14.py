import aoc
data = aoc.strlist(14)

x, y = {}, {}
for p, q in (i.split(" = ") for i in data):
    if p == "mask":
        u = int(q.replace("X", "1"), 2)
        v = int(q.replace("X", "0"), 2)
        m = q
    else:
        x[int(p[4:-1])] = int(q) & u | v
        a = "{:036b}".format(int(p[4:-1]) | v)
        s = set([""])
        for j in range(36):
            s = {k + "0" for k in s} | {k + "1" for k in s} if m[j] == "X" else {k + a[j] for k in s}
        for k in s:
            y[int(k, 2)] = int(q)

print(sum(x.values()), sum(y.values()))
aoc.tock("ms")
