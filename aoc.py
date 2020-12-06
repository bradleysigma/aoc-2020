from time import time
t = time()
def tock(units="s"):
    print(f'{(time() - t) * {"h": 1/3600, "m": 1/60, "s": 1, "ms": 1000, "us": 1e6}[units]:.2f}{units}')

import urllib.request, urllib.error

def read(n):
    f = open("input"+str(n)+".txt")
    s = f.read()
    f.close()
    return s

def itterlist(n, t=list):
    return t(map(int, read(n).strip("\n").split("\n")))

def strlist(n, t=list):
    return t(read(n).strip("\n").split("\n"))

def strgroups(n, t=list):
    return t(i.split("\n") for i in read(n).strip("\n").split("\n\n"))
