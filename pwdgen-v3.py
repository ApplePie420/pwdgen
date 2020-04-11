import re
import itertools
from multiprocessing import Process

azAZ = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!"

def betterComb(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    for indicies in itertools.product(range(n), r):
        if sorted(indicies) == list(indicies):
            yield tuple(pool[i] for i in indicies)

def getAI():
    f = open("listAI.txt", "w")
    for result in itertools.product(azAZ, repeat=10):
        kek = ""
        for i in range(0, 10):
            kek += str(result[i])
        regex = re.search("[A-i][a-i][a-i][a-i][a-i][0-9][0-9][0-9][0-9](!)", str(kek))
        if regex:
            f.write(regex.group(0) + "\n")
    f.close()

def getJQ():
    f = open("listJQ.txt", "w")
    for result in itertools.product(azAZ, repeat=10):
        kek = ""
        for i in range(0, 10):
            kek += str(result[i])
        regex = re.search("[J-Q][j-q][j-q][j-q][j-q][0-9][0-9][0-9][0-9](!)", str(kek))
        if regex:
            f.write(regex.group(0) + "\n")
    f.close()

def getRZ():
    f = open("listRZ.txt", "w")
    for result in itertools.product(azAZ, repeat=10):
        kek = ""
        for i in range(0, 10):
            kek += str(result[i])
        regex = re.search("[R-Z][r-z][r-z][r-z][r-z][0-9][0-9][0-9][0-9](!)", str(kek))
        if regex:
            f.write(regex.group(0) + "\n")
    f.close()

if __name__ == "__main__":
    for i in range(3):
        p = Process(target=getAI)
        q = Process(target=getJQ)
        r = Process(target=getRZ)
        p.start()
        q.start()
        r.start()




""" f = open("list.txt", "w")

for result in itertools.product(azAZ, repeat=10):
    kek = ""
    for i in range(0, 10):
        kek += str(result[i])
    regex = re.search("[A-Z][a-z][a-z][a-z][a-z][0-9][0-9][0-9][0-9](!)", str(kek))
    if regex:
        #print(regex.group(0))
        f.write(regex.group(0) + "\n")

f.close() """