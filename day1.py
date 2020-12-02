import aoc

x = aoc.itterlist(1, set)

def p1(x):
    for i in x:
        if 2020-i in x:
            print(i*(2020-i))
            return
def p2(x):
    for i in x:
        for j in x:
            if 2020-i-j in x:
                print(i*j*(2020-i-j))
                return

p1(x)
p2(x)

aoc.tock()
