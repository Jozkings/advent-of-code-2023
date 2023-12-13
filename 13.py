from typing import Dict, List, Tuple

FILE_NAME = 'input13.in'

res1 = 0
res2 = 0


def check_mirror_horizontal(mapo: List[str], mirror: Tuple[int, int]) -> int:
    a, b = mirror
    while a >= 0 and b < len(mapo):
        if mapo[a] != mapo[b]:
            return 0
        a -= 1
        b += 1
    return mirror[0] + 1


def horizontal_reflection(mapo: List[str], map_index: int, clean_mirrors: Dict[int, Tuple[Tuple[int, int], bool]],
                          is_vertical: bool=False) -> int:
    for i in range(1, len(mapo)):
        if mapo[i] == mapo[i-1]:
            mirror = (i-1, i)
            res = check_mirror_horizontal(mapo, mirror)
            if res:
                if map_index not in clean_mirrors.keys():
                    clean_mirrors[map_index] = (mirror, is_vertical)
                elif (mirror, is_vertical) == clean_mirrors[map_index]:
                    continue
                return res * 100 if not is_vertical else res
    return 0


def vertical_reflection(mapo: List[str], map_index: int, clean_mirrors: Dict[int, Tuple[Tuple[int, int], bool]],
                        is_vertical: bool = True) -> int:
    return horizontal_reflection(mapo, map_index, clean_mirrors, is_vertical)


def trans_array(mapo: List[str]) -> List[str]:
    return [''.join([mapo[i][j] for i in range(len(mapo))]) for j in range(len(mapo[0]))]


def reflection(mapo: List[str], map_index: int, clean_mirrors: Dict[int, Tuple[Tuple[int, int], bool]]) -> int:
    return (horizontal_reflection(mapo, map_index, clean_mirrors) +
            vertical_reflection(trans_array(mapo), map_index, clean_mirrors))


def get_new_mapo(mapo: List[str], a: int, b: int) -> List[str]:
    new_mapo = []
    for i in range(len(mapo)):
        if i != a:
            new_mapo.append(mapo[i])
        else:
            special = '.' if mapo[i][b] == '#' else '#'
            new_mapo.append(mapo[i][:b] + special + mapo[i][b+1:])
    return new_mapo


def smudge_reflection(mapo: List[str], map_index: int, clean_mirrors: Dict[int, Tuple[Tuple[int, int], bool]]) -> int:
    for i in range(len(mapo)):
        for j in range(len(mapo[0])):
            new_mapo = get_new_mapo(mapo, i, j)
            res = reflection(new_mapo, map_index, clean_mirrors)
            if res:
                return res
    return 0

mapo = []
clean_mirrors = {}


with open(FILE_NAME, 'r') as file:
    for index, line in enumerate(file):
        value = line.strip()
        if not value:
            res1 += reflection(mapo, index, clean_mirrors)
            res2 += smudge_reflection(mapo, index, clean_mirrors)
            mapo = []
        else:
            mapo.append(value)

res1 += reflection(mapo, index, clean_mirrors)
res2 += smudge_reflection(mapo, index, clean_mirrors)

print(res1)
print(res2)