import aoc
data = aoc.strgroups(4)

n = 0
m = 0
for i in data:
    f = {}
    for j in " ".join(i).split(" "):
        k, v = j.split(":")
        if k == "cid": continue
        f[k] = v
    if set(f.keys()) == {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}:
        n += 1
        b = True
        b = b and 1920 <= int(f["byr"]) <= 2002
        b = b and 2010 <= int(f["iyr"]) <= 2020
        b = b and 2020 <= int(f["eyr"]) <= 2030
        if f["hgt"][-2:] == "cm":
            b = b and 150 <= int(f["hgt"][:-2]) <= 193
        elif f["hgt"][-2:] == "in":
            b = b and 59 <= int(f["hgt"][:-2]) <= 76
        else:
            b = False
        b = b and len(f["hcl"]) == 7 and f["hcl"][0] == "#" and set(f["hcl"][1:]) <= set("0123456789abcdef")
        b = b and f["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        b = b and len(f["pid"]) == 9 and set(f["pid"]) <= set("0123456789")
        if b: m += 1

print(n)
print(m)

aoc.tock("ms")
