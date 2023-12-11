from typing import List, Tuple

FILE_NAME = 'input11.in'

res1 = 0
res2 = 0

galaxies = []

with open(FILE_NAME, 'r') as file:
    for i, line in enumerate(file):
        value = line.strip()
        j = 0
        for j, charo in enumerate(value):
            if charo == '#':
                galaxies.append((i, j))


def expand_map(galaxies: List[Tuple[int, int]], adding: int=2) -> List[Tuple[int, int]]:
    actual_galaxies = galaxies[:]
    expansion = adding - 1
    new_galaxies = []
    galaxy_rows_i = [g[0] for g in actual_galaxies]
    galaxy_rows_j = [g[1] for g in actual_galaxies]

    shift = 0
    for i in range(len(galaxies)):
        diff = galaxy_rows_i[i] - (galaxy_rows_i[i-1] if i > 0 else -1)
        shift += expansion * (max(diff-1, 0))
        this_galaxy = galaxy_rows_i[i] + shift
        new_galaxies.append((this_galaxy, galaxy_rows_j[i]))

    actual_galaxies = new_galaxies[:]
    new_galaxies = []
    galaxies_sorted = sorted(actual_galaxies, key=lambda val: val[1])

    galaxy_rows_i = [g[0] for g in galaxies_sorted]
    galaxy_rows_j = [g[1] for g in galaxies_sorted]

    shift = 0
    for j in range(len(galaxies)):
        diff = galaxy_rows_j[j] - (galaxy_rows_j[j - 1] if j > 0 else -1)
        shift += expansion * (max(diff-1, 0))
        this_galaxy = galaxy_rows_j[j] + shift
        new_galaxies.append((galaxy_rows_i[j], this_galaxy))

    return new_galaxies


def get_manhattan_distance(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1-x2) + abs(y1-y2)


def get_distances(galaxies: List[Tuple[int, int]]) -> List[int]:
    distances = []
    for i, fgalaxy in enumerate(galaxies):
        for j, sgalaxy in enumerate(galaxies):
            if i < j:
                gal1x, gal1y = fgalaxy
                gal2x, gal2y = sgalaxy
                distances.append(get_manhattan_distance(gal1x, gal1y, gal2x, gal2y))
    return distances


first_galaxies = expand_map(galaxies)
res1 = sum(get_distances(first_galaxies))

print(res1)

second_galaxies = expand_map(galaxies, 1000000)
res2 = sum(get_distances(second_galaxies))
print(res2)


