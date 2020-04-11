import re
import itertools

azAZ = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!"

def betterComb(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    for indicies in itertools.product(range(n), r):
        if sorted(indicies) == list(indicies):
            yield tuple(pool[i] for i in indicies)

n = 5

f = open("list.txt", "w")

for result in itertools.product(azAZ, repeat=10):
    kek = ""
    for i in range(0, 10):
        kek += str(result[i])
    regex = re.search("[A-Z][a-z][a-z][a-z][a-z][0-9][0-9][0-9][0-9](!)", str(kek))
    if regex:
        #print(regex.group(0))
        f.write(regex.group(0) + "\n")

f.close()