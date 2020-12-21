import aoc
from itertools import product
data = aoc.strgroups(19)
rules, message = data

d = {}
while rules:
    i = rules.pop(0)
    num, match = i.split(": ")
    num = int(num)
    if any(j.isnumeric() and int(j) not in d for j in match.split(" ")):
        rules.append(i)
        continue
    if "\"" in match:
        d[num] = set([match.strip("\"")])
        continue
    d[num] = set()
    for j in match.split(" | "):
        d[num] |= set("".join(k) for k in product(*(map(d.get, map(int, j.split(" "))))))

n = 0
m = 0
for i in message:
    n += int(i in d[0])
    if not any(i.startswith(j) for j in d[42]) or not any(i.endswith(j) for j in d[31]): continue
    while any(i.startswith(j) for j in d[42]) and any(i.endswith(j) for j in d[31]):
        i = i[8:-8]
    if not any(i.startswith(j) for j in d[42]): continue
    while any(i.startswith(j) for j in d[42]):
        i = i[8:]
    m += int(not i)

print(n, m)
aoc.tock()
