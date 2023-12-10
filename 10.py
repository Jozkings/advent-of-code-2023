from collections import defaultdict as dd
from typing import DefaultDict, Tuple, List, Dict, Set

FILE_NAME = 'input10.in'

res1 = 0
res2 = 0


def pos_to_string(pos: Tuple[int, int]) -> str:
    return str(pos[0]) + "," + str(pos[1])


def string_to_pos(string: str) -> Tuple[int, int]:
    return tuple(map(int, string.split(",")))


def sum_tuples(*args: List[Tuple[int, int]]) -> Tuple[int, int]:
    return tuple(map(sum, zip(*args)))


def get_neighbours(i: int, j: int) -> List[Tuple[int, int]]:
    return [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]


def get_starting_possibles(pos: Tuple[int, int]) -> List[Tuple[int, int]]:
    res = []
    for neigh in get_neighbours(0, 0):
        new_pos = sum_tuples(pos, neigh)
        if neigh[1] and mapo[new_pos] in ["|", "."]:
            continue
        elif neigh[0] and mapo[new_pos] in ["-", "."]:
            continue
        res.append(neigh)
    return res


def get_all_points(mapo: DefaultDict[Tuple[int, int], str], changes: Dict[str, List[Tuple[int, int]]],
                   x: int, y: int, i: int, j: int) -> List[Tuple[int, int]]:
    if mapo[(i,j)] == '.':
        return []
    if mapo[(i,j)] in changes.keys():
        return [sum_tuples((x, y), (cx, cy)) for (cx, cy) in changes[mapo[(i,j)]]]
    return [(a, b) for a, b in get_neighbours(x, y) if (i, j) in mapo]  # S


def continue_condition_loop(mapo: DefaultDict[Tuple[int, int], str], new_pos: Tuple[int, int],
                            last_pos: Tuple[int, int]) -> bool:
    if new_pos == last_pos:
        return True
    if new_pos not in mapo:
        return True
    if mapo[new_pos] == ".":
        return True
    return False


def continue_condition_enclosed(pos: Tuple[int, int], boundaries, visited) -> bool:
    if pos in boundaries:
        return True
    if pos in visited:
        return True
    return False


def get_loop(queue: List[Tuple[Tuple[int, int], str, int, Tuple[int, int]]],
             mapo: DefaultDict[Tuple[int, int], str]) -> Tuple[str, int]:
    loop_string = None
    path_length = 0

    while queue:
        current_pos, current_path, path_length, last_pos = queue.pop(0)
        current_value = mapo[current_pos]

        if current_value == "S":
            if last_pos is not None:
                loop_string = current_path
                break
            possibles = get_starting_possibles(current_pos)
        else:
            possibles = changes[current_value]
        for change in possibles:
            new_pos = sum_tuples(current_pos, change)
            if continue_condition_loop(mapo, new_pos, last_pos):
                continue
            queue.append((new_pos, current_path + "#" + pos_to_string(new_pos), path_length + 1, current_pos))

    return loop_string, path_length // 2


def get_enclosed_size(queue: List[Tuple[int, int]], boundaries: Set[Tuple[int, int]],
                      visited: Set[Tuple[int, int]]) -> int:
    res = queue[0][0] % 2 == 0 and queue[0][1] % 2 == 0
    while queue:
        i, j = queue.pop(0)
        for neighbour in get_neighbours(i, j):
            if continue_condition_enclosed(neighbour, boundaries, visited):
                continue
            if neighbour == (0, 0):
                return 0
            queue.append(neighbour)
            visited.add(neighbour)
            res += neighbour[0] % 2 == 0 and neighbour[1] % 2 == 0
    return res


changes = {"|": [(-1,0), (1,0)], "-": [(0,-1), (0,1)],  "L": [(-1,0), (0,1)], "J": [(-1,0), (0,-1)],
           "7": [(1,0), (0,-1)], "F": [(1,0), (0,1)]}
mapo = dd(str)
animal_start = (0, 0)

with open(FILE_NAME, 'r') as file:
    for i, line in enumerate(file):
        value = line.strip()
        for j in range(len(value)):
            mapo[(i, j)] = value[j]
            if value[j] == "S":
                animal_start = (i, j)

queue = [(animal_start, pos_to_string(animal_start), 0, None)]  #current_pos, current_path, last_pos, path_length
loop_string, res1 = get_loop(queue, mapo)
print(res1)

loop = [string_to_pos(item) for item in loop_string.split("#")]
bigger_loop = [(2 * i, 2 * j) for (i, j) in loop]
new_loop = []

for bi, bj in bigger_loop:
    si = bi // 2
    sj = bj // 2
    for neighbor in get_all_points(mapo, changes, bi, bj, si, sj):
        new_loop.append(neighbor)

boundaries = set(bigger_loop + new_loop)
sx, sy = animal_start
starts = {(2 * sx + 1, 2 * sy + 1), (2 * sx - 1, 2 * sy + 1), (2 * sx + 1, 2 * sy - 1), (2 * sx - 1, 2 * sy - 1)}

for start in starts:
    res2 = max(res2, get_enclosed_size([start], boundaries, {start}))

print(res2)