import aoc
data = aoc.strlist(8)

instruc = [(i.split(" ")[0], int(i.split(" ")[1])) for i in data]

accx = 0
point = 0
seen = set()
while point not in seen:
    seen.add(point)
    i, j = instruc[point]
    point += j if i == "jmp" else 1
    accx += j if i == "acc" else 0

for k in range(len(instruc)):
    if instruc[k][0] == "acc": continue
    if instruc[k][1] in [0, 1]: continue
    alter = list(instruc)
    alter[k] = ("nop" if alter[k][0] == "jmp" else "jmp", alter[k][1])

    accy = 0
    point = 0
    seen = set()
    while point not in seen:
        seen.add(point)
        i, j = alter[point]
        point += j if i == "jmp" else 1
        accy += j if i == "acc" else 0
        if point >= len(alter): break
    else:
        continue
    break

print(accx, accy)
aoc.tock("ms")
