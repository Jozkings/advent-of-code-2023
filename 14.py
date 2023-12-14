from collections import defaultdict as dd
from typing import DefaultDict, List, Tuple

FILE_NAME = 'input14.in'

res1 = 0
res2 = 0


def shift(mapo: DefaultDict[Tuple[int, int], str], keys: List[Tuple[int, int]], changes: Tuple[int, int])\
        -> DefaultDict[Tuple[int, int], str]:
    new_mapo = dd(str)
    xchange, ychange = changes
    for key in keys:
        value = mapo[key]
        if value == 'O':
            x, y = key
            while True:
                new_x, new_y = x + xchange, y + ychange
                if (new_x, new_y) not in mapo or ((new_x, new_y) in new_mapo and new_mapo[(new_x, new_y)] != '.'):
                    break
                x = new_x
                y = new_y
            new_mapo[(x, y)] = 'O'
            if key != (x, y):
                new_mapo[key] = '.'
        else:
            if value == "#":
                new_mapo[key] = '#'
            else:
                if key in new_mapo:
                    continue
                new_mapo[key] = '.'
    return new_mapo


def cycle(mapo: DefaultDict[Tuple[int, int], str]) -> DefaultDict[Tuple[int, int], str]:
    mapo = shift(mapo, nkeys, nchanges)
    mapo = shift(mapo, wkeys, wchanges)
    mapo = shift(mapo, skeys, schanges)
    mapo = shift(mapo, ekeys, echanges)
    return mapo


mapo = dd(str)
max_i, max_j = 0, 0

with open(FILE_NAME, 'r') as file:
    for index, line in enumerate(file):
        value = line.strip()
        for j, charo in enumerate(value):
            mapo[(index, j)] = charo
        max_j = j + 1
        max_i = index + 1

nkeys = [(x, y) for x in range(max_i) for y in range(max_j)]
wkeys = [(y, x) for x in range(max_i) for y in range(max_j)]
ekeys = [(y, x) for x in range(max_i - 1, -1, -1) for y in range(max_j)]
skeys = [(x, y) for x in range(max_i - 1, -1, -1) for y in range(max_j)]

nchanges = (-1, 0)
wchanges = (0, -1)
echanges = (0, 1)
schanges = (1, 0)

res1 = sum(max_i - key[0] for key, value in shift(mapo, nkeys, nchanges).items() if value == "O")
print(res1)

cycles = 1000000000
all_maps = dd(int)
current = 0

while current < cycles:
    mapo = cycle(mapo)
    s_mapo = str(mapo)

    if s_mapo in all_maps:
        index = all_maps[s_mapo]
        diff = current - index
        rest = cycles - ((cycles - index) // diff) * diff - index - 1
        for i in range(rest):
            mapo = cycle(mapo)
        break
    else:
        all_maps[s_mapo] = current
    current += 1

res2 = sum(max_i - key[0] for key, value in mapo.items() if value == "O")
print(res2)
