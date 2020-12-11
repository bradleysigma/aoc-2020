import aoc
data = aoc.strlist(8)

instruc = [(i.split(" ")[0], int(i.split(" ")[1])) for i in data]

acc = 0
point = 0
seen = set()
while point not in seen:
    seen.add(point)
    i, j = instruc[point]
    if i == "jmp":
        point += j
    elif i == "acc":
        acc += j
        point += 1
    elif i == "nop":
        point += 1
    else:
        print(i)
        point += 1
print(acc)

for k in range(len(instruc)):
    if instruc[k][0] == "acc": continue
    if instruc[k][1] in [0, 1]: continue
    alter = list(instruc)
    if alter[k][0] == "jmp":
        alter[k] = ("nop", alter[k][1])
    elif alter[k][0] == "nop":
        alter[k] = ("jmp", alter[k][1])
    else:
        print(alter[k])

    acc = 0
    point = 0
    seen = set()
    while point not in seen:
        seen.add(point)
        i, j = alter[point]
        if i == "jmp":
            point += j
        elif i == "acc":
            acc += j
            point += 1
        elif i == "nop":
            point += 1
        else:
            print(i)
            point += 1
        if point >= len(alter):
            print(acc)
            break

aoc.tock("ms")
