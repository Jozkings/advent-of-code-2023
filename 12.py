from typing import Dict, Tuple

FILE_NAME = 'input12.in'

res1 = 0
res2 = 0


def get_springs(springs: str, repeat: int = 1) -> str:
    return ((springs + "?") * repeat)[:-1]


def get_groups(groups: str, repeat: int = 1) -> Tuple[int, ...]:  # cannot be list
    return tuple(map(int, ((groups + ",") * repeat)[:-1].split(",")))


def recursive(memo: Dict[Tuple[str, Tuple[int, ...]], int], springs: str, groups: Tuple[int, ...]) -> int:
    if len(springs) == 0:
        memo[(springs, groups)] = (len(groups) == 0)

    if (springs, groups) in memo:
        return memo[(springs, groups)]

    match springs[0]:
        case ".":
            memo[(springs, groups)] = recursive(memo, springs[1:], groups)
        case "#":
            if len(groups) == 0 or len(springs) < groups[0]:
                memo[(springs, groups)] = 0
            elif springs[:groups[0]].count(".") > 0:
                memo[(springs, groups)] = 0
            elif len(groups) == 1:
                memo[(springs, groups)] = recursive(memo, springs[groups[0]:], groups[1:])
            elif len(springs) < groups[0] + 1 or springs[groups[0]] == "#":
                memo[(springs, groups)] = 0
            else:
                memo[(springs, groups)] = recursive(memo, springs[groups[0] + 1:], groups[1:])
        case "?":
            memo[(springs, groups)] = (recursive(memo, "." + springs[1:], groups)
                                       + recursive(memo, "#" + springs[1:], groups))
    return memo[(springs, groups)]


with open(FILE_NAME, 'r') as file:
    for index, line in enumerate(file):
        value = line.strip().split()
        res1 += recursive({}, get_springs(value[0]), get_groups(value[1]))
        res2 += recursive({}, get_springs(value[0], repeat=5), get_groups(value[1], repeat=5))

print(res1)
print(res2)
