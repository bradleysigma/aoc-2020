import aoc
data = aoc.strlist(18)

y = 0
z = 0
for i, j in zip(data, data):
    i = "(" + i + ")"
    while not i.isnumeric():
        n, m = -1, len(i)
        while "(" in i[n+1:m]:
            n = i.index("(", n+1)
            m = i.index(")", n+1)
        p = i[n+1:m].split(" ")
        while len(p) > 1:
            p[:3] = [(int(p[0]) + int(p[2])) if p[1] == "+" else (int(p[0]) * int(p[2]))]
        i = i[:n] + str(p[0]) + i[m+1:]
    y += int(i)

    j = "(" + j + ")"
    while not j.isnumeric():
        n, m = -1, len(j)
        while "(" in j[n+1:m]:
            n = j.index("(", n+1)
            m = j.index(")", n+1)
        q = j[n+1:m].split(" ")
        while "+" in q:
            t = q.index("+")
            q[t-1:t+2] = [int(q[t-1]) + int(q[t+1])]
        while "*" in q:
            t = q.index("*")
            q[t-1:t+2] = [int(q[t-1]) * int(q[t+1])]
        j = j[:n] + str(q[0]) + j[m+1:]
    z += int(j)

print(y, z)
aoc.tock("ms")
