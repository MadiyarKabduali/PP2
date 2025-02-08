import itertools
def permut(s):
    return list(map("".join, itertools.permutations(s)))
print(permut("Madi"))