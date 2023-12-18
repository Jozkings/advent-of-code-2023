from typing import List, Tuple

FILE_NAME = 'input18.in'

res1 = 0
res2 = 0


def sum_tuples(*args: Tuple[int, int]) -> Tuple[int, int]:
    return tuple(map(sum, zip(*args)))


def shoelace(points: List[Tuple[int, int]]) -> int:
    x, y = zip(*points)
    return int(0.5 * abs(
        sum(x[i] * y[i - 1] - x[i - 1] * y[i] for i in range(len(points))))
    )


def picks_theorem(a: int, b: int) -> int:
    return a - b//2 + 1


def get_hexa_data(hexa: str) -> Tuple[str, int]:
    hexa = hexa[2:-1]
    return hexa[-1], int(hexa[:-1], 16)


def get_cubic_meters(data: List[List[str]], is_hexa: bool = False) -> int:
    dir_change = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
    number_dir_change = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}

    current_position = (0, 0)
    vertices = []
    edges_length = 0

    for value in data:
        dir, length, rgb = value

        if is_hexa:
            dir, length = get_hexa_data(rgb)
            dir = number_dir_change[dir]
        change = tuple([int(length) * x for x in dir_change[dir]])
        edges_length += int(length)

        current_position = sum_tuples(current_position, change)
        vertices.append(current_position)

    polyarea = shoelace(vertices)
    inside = picks_theorem(polyarea, edges_length)

    return int(edges_length + inside)


lines = []


with open(FILE_NAME, 'r') as file:
    for index, line in enumerate(file):
        lines.append(line.strip().split())


res1 = get_cubic_meters(lines)
res2 = get_cubic_meters(lines, is_hexa=True)

print(res1)
print(res2)
