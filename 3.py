from collections import defaultdict as dd
from typing import List, Tuple, DefaultDict

FILE_NAME = 'input3.in'

res1 = 0
res2 = 0

mapo = dd(str)
gears = dd(list)
max_i, max_j = 0, 0


def get_number(mapo: DefaultDict[Tuple[int, int], str], indeces: List[Tuple[int, int]]) -> int:
    return int(''.join(map(lambda x: mapo[x], indeces)))


def get_neighbours(i: int, j: int) -> List[Tuple[int, int]]:
    return [(i, j-1), (i, j+1), (i-1, j), (i+1, j),
            (i-1, j-1), (i+1, j+1), (i-1, j+1), (i+1, j-1)]


def check_numbers_and_gears(mapo: DefaultDict[Tuple[int, int], str], adjacent: bool, indeces: List[Tuple[int, int]],
                            gear: Tuple[int, int]) -> Tuple[int, bool]:
    engine, is_gear_part = 0, False
    if adjacent and indeces:
        engine = get_number(mapo, indeces)
        if gear is not None:
            is_gear_part = True
    return engine, is_gear_part


with open(FILE_NAME, 'r') as file:
    for i, line in enumerate(file):
        j = 0
        value = line.strip()
        for j, val in enumerate(value):
            mapo[(i, j)] = val
        max_i = i
        max_j = j


current_indeces = []
adjacent = False
current_gear = None

for i in range(max_i + 1):
    for j in range(max_j + 1):
        if not mapo[(i, j)].isnumeric():
            engine, is_gear_part = check_numbers_and_gears(mapo, adjacent, current_indeces, current_gear)
            res1 += engine
            if engine and is_gear_part:
                gears[current_gear].append(engine)

            current_indeces = []
            adjacent = False
            current_gear = None
        else:
            current_indeces.append((i, j))
            neighs = get_neighbours(i, j)

            for neigh in neighs:
                if neigh in mapo and not mapo[neigh].isnumeric() and mapo[neigh] != '.':
                    adjacent = True
                    if mapo[neigh] == '*':
                        current_gear = neigh
                    break

engine, is_gear_part = check_numbers_and_gears(mapo, adjacent, current_indeces, current_gear)
res1 += engine
if engine and is_gear_part:
    gears[current_gear].append(engine)

res2 = sum(map(lambda x: x[0] * x[1] if len(x) == 2 else 0, gears.values()))

print(res1)
print(res2)

