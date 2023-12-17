from collections import defaultdict as dd
import heapq
from typing import DefaultDict, List, Tuple

FILE_NAME = 'input17.in'

res1 = 0
res2 = 0

mapo = dd(int)
max_i, max_j = 0, 0


def get_dirs() -> List[Tuple[int, int]]:
    return [(0, 1), (1, 0), (0, -1), (-1, 0)]


def sum_tuples(*args: Tuple[int, int]) -> Tuple[int, int]:
    return tuple(map(sum, zip(*args)))


def dijkstra(mapo: DefaultDict[Tuple[int, int], int], start: Tuple[int, int], end: Tuple[int, int], minimum: int,
             maximum: int) -> int:
    queue = [(0, start, None)]  # (cost, pos, dir)
    visited = set()
    losses = dd(int)

    while queue:
        cost, pos, dir = heapq.heappop(queue)
        if pos == end:
            return cost

        if (pos, dir) in visited:
            continue
        visited.add((pos, dir))

        for neigh in get_dirs():
            dx, dy = neigh
            reverse = (-dx, -dy)
            if dir == reverse or dir == neigh:
                continue

            loss = 0
            for distance in range(1, maximum + 1):
                new_pos = sum_tuples(pos, (dx * distance, dy * distance))
                if new_pos not in mapo:
                    break
                loss += mapo[new_pos]
                if minimum and distance < minimum:
                    continue
                new_cost = cost + loss
                if (new_pos, neigh) in losses and losses[(new_pos, neigh)] <= new_cost:
                    continue
                losses[(new_pos, neigh)] = new_cost
                heapq.heappush(queue, (new_cost, new_pos, neigh))


with open(FILE_NAME, 'r') as file:
    for index, line in enumerate(file):
        value = line.strip()
        for j, char in enumerate(value):
            mapo[(index, j)] = int(char)
            max_j = j
        max_i = index


start = (0, 0)
end = (max_i, max_j)

res1 = dijkstra(mapo, start, end, 0, 3)
res2 = dijkstra(mapo, start, end, 4, 10)


print(res1)
print(res2)
