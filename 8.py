from collections import defaultdict as dd
from math import lcm
from typing import DefaultDict, Tuple, Set, List

FILE_NAME = 'input8.in'

res1 = 0
res2 = 0

dirs_line = True
dirs = ""
network = dd(tuple)


def get_starts_and_ends(keys: List[str]) -> Tuple[List[str], Set[str]]:
    starts = []
    ends = set()
    for key in keys:
        if key[-1] == "A":
            starts.append(key)
        elif key[-1] == "Z":
            ends.add(key)
    return starts, ends


def get_steps(network: DefaultDict[str, Tuple[str, str]], dirs: str, starts: List[str], ends: Set[str]) -> int:
    cur_index = 0
    current_step = 0
    running = True

    currents = [starts[i] for i in range(len(starts))]
    steps = [None for _ in range(len(starts))]

    while running:
        running = False
        for i, current in enumerate(currents):
            if steps[i] is not None:
                continue
            left, right = network[current]
            diro = dirs[cur_index]
            current = left if diro == 'L' else right
            currents[i] = current
            if current in ends:
                steps[i] = current_step + 1
                continue
            running = True

        current_step += 1
        cur_index = (cur_index + 1) % len(dirs)

    return lcm(*steps)


with open(FILE_NAME, 'r') as file:
    for index, line in enumerate(file):
        value = line.strip()
        if dirs_line:
            dirs_line = False
            dirs = value
        elif value:
            val = value.split(" = ")
            val[1] = val[1].split(", ")
            left, right = val[1][0][1:], val[1][1][:-1]
            network[val[0]] = (left, right)


starts, ends = ['AAA'], {'ZZZ'}
res1 = get_steps(network, dirs, starts, ends)
print(res1)

starts, ends = get_starts_and_ends(network.keys())
res2 = get_steps(network, dirs, starts, ends)
print(res2)