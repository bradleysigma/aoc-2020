import aoc
data = aoc.intlist(9)

for i in range(25, len(data)):
    for j in range(i-25, i):
        if data[i]-data[j] in data[j:i]:
            break
    else:
        n = data[i]
        break

for i in range(len(data)):
    m = n
    j = 0
    while m > 0:
        m -= data[i+j]
        j += 1
    if m == 0 and j > 1:
        print(n, max(data[i:i+j]) + min(data[i:i+j]))

aoc.tock("ms")
