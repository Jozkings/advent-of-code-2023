from collections import defaultdict as dd
from collections.abc import Iterator
from typing import Tuple

FILE_NAME = 'input16.in'

res1 = 0
res2 = 0

dirs = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
splitters = ['|', '-']
mirrors = ['/', '\\']
mirror_change = {"R/": "U", "R\\": "D", "L/": "D", "L\\": "U",
                 "U/": "R", "U\\": "L", "D/": "L", "D\\": "R"}

mapo = dd(str)


def sum_tuples(*args: Tuple[int, int]) -> Tuple[int, int]:
    return tuple(map(sum, zip(*args)))


def is_pointy(dir: str, splitter: str) -> bool:
    return (dir in ['L', 'R'] and splitter == '-') or (dir in ['U', 'D'] and splitter == '|')


def split(splitter: str) -> Tuple[str, str]:
    return ('L', 'R') if splitter == '-' else ('U', 'D')


def get_starts(max_i: int, max_j: int) -> Iterator[Tuple[Tuple[int, int], str]]:
    for i in range(max_i):
        yield (i, 0), 'R'
        yield (i, max_j - 1), 'L'
    for j in range(max_j):
        yield (0, j), 'D'
        yield (max_i - 1, j), 'U'


with open(FILE_NAME, 'r') as file:
    for index, line in enumerate(file):
        value = line.strip()
        for j, charo in enumerate(value):
            mapo[(index, j)] = charo
            max_j = j + 1
        max_i = index + 1


for start, dir in get_starts(max_i, max_j):
    visited = set()
    energized = set()
    queue = [(start, dir)]
    while queue:
        current, dir = queue.pop(0)
        if current not in mapo or (current, dir) in visited:
            continue

        visited.add((current, dir))
        energized.add(current)
        charo = mapo[current]

        if charo in mirrors:
            dir = mirror_change[dir + charo]
            new = sum_tuples(current, dirs[dir])
            queue.append((new, dir))

        elif charo in splitters:
            if is_pointy(dir, charo):
                new = sum_tuples(current, dirs[dir])
                queue.append((new, dir))
            else:
                for dir in split(charo):
                    new = sum_tuples(current, dirs[dir])
                    queue.append((new, dir))
        else:
            new = sum_tuples(current, dirs[dir])
            queue.append((new, dir))

    res2 = max(res2, len(energized))
    if start == (0, 0) and dir == 'R':
        res1 = len(energized)


print(res1)
print(res2)
