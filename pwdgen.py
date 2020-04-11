import itertools


def betterComb(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    for indicies in itertools.permutations(range(n), r):
        if sorted(indicies) == list(indicies):
            yield tuple(pool[i] for i in indicies)

f = open("list.txt", "w")
n = 10

for result in betterComb("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!", n):
    for i in range(0, n):
        f.write(str(result[i]))
    f.write("\n")

f.close()