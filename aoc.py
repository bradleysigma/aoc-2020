from time import time
t = time()
def tock():
    print(time() - t)

def read(n):
    f = open("input"+str(n)+".txt")
    s = f.read()
    f.close()
    return s

def itterlist(n, t=list):
    return t(map(int, read(n).strip("\n").split("\n")))

def strlist(n, t=list):
    return t(read(n).strip("\n").split("\n"))

