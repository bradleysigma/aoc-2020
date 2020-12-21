import aoc
data = aoc.strlist(18)

y = 0
z = 0
for i, j in zip(data, data):
    i = "(" + i + ")"
    while i[0] == "(":
        m = i.index(")")
        n = i[:m].rindex("(")
        p = i[n+1:m].split(" ")
        while len(p) > 1:
            p[:3] = [(int(p[0]) + int(p[2])) if p[1] == "+" else (int(p[0]) * int(p[2]))]
        i = i[:n] + str(p[0]) + i[m+1:]
    y += int(i)

    j = "(" + j + ")"
    while j[0] == "(":
        m = j.index(")")
        n = j[:m].rindex("(")
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
