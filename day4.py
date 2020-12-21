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
        m += all([1920 <= int(f["byr"]) <= 2002,
                  2010 <= int(f["iyr"]) <= 2020,
                  2020 <= int(f["eyr"]) <= 2030,
                  any([f["hgt"][-2:] == "cm" and 150 <= int(f["hgt"][:-2]) <= 193,
                       f["hgt"][-2:] == "in" and 59 <= int(f["hgt"][:-2]) <= 76]),
                  len(f["hcl"]) == 7 and f["hcl"][0] == "#" and set(f["hcl"][1:]) <= set("0123456789abcdef"),
                  f["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
                  len(f["pid"]) == 9 and set(f["pid"]) <= set("0123456789")])

print(n, m)
aoc.tock("ms")
