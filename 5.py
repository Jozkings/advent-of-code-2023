from collections import defaultdict as dd
from typing import DefaultDict, Tuple, List, Dict

FILE_NAME = 'input5.in'

res1 = 0
res2 = 0

keymap = {'seeds': 'seed-to-soil', 'seed-to-soil': 'soil-to-fertilizer', 'soil-to-fertilizer': 'fertilizer-to-water',
          'fertilizer-to-water': 'water-to-light', 'water-to-light': 'light-to-temperature',
          'light-to-temperature': 'temperature-to-humidity', 'temperature-to-humidity': 'humidity-to-location',
          'humidity-to-location': 'end'}


seed_line = True
current_key = ''
mappings = dd(list)


def determine_location(number: int, mappings: DefaultDict[str, List[Tuple[range, int]]], keymap: Dict[str, str]) -> int:
    current_key = 'seeds'
    while current_key != 'end':
        for (cur_range, dest) in mappings[current_key]:
            if number in cur_range:
                number = dest + number - cur_range[0]
                break
        current_key = keymap[current_key]
    return number


def determine_location_ranges(ranges: List[range], mappings: DefaultDict[str, List[Tuple[range, int]]], keymap: Dict[
    str, str]) -> List[range]:
    current_key = 'seeds'
    while current_key != 'end':
        ranges = get_ranges(ranges, mappings[current_key])
        current_key = keymap[current_key]
    return ranges


def get_ranges(remaining: List[range], map_ranges: List[Tuple[range, int]]) -> List[range]:
    result = []
    for (cur_range, dest) in map_ranges:
        nexto = []
        for remain in remaining:
            if remain[-1] < cur_range[0] or cur_range[-1] < remain[0]:
                nexto.append(remain)
            elif cur_range[0] <= remain[0] and remain[-1] <= cur_range[-1]:
                start = remain[0] + dest - cur_range[0]
                result.append(range(start, start + len(remain)))
            elif remain[0] < cur_range[0] and cur_range[-1] < remain[-1]:
                result.append(range(dest, dest + len(cur_range)))
                nexto.append(range(remain[0], cur_range[0]))
                nexto.append(range(cur_range[-1] + 1, remain[-1] + 1))
            elif cur_range[0] <= remain[0] <= cur_range[-1] < remain[-1]:
                nexto.append(range(cur_range[-1] + 1, remain[-1] + 1))
                start = dest + remain[0] - cur_range[0]
                end = dest + len(cur_range)
                result.append(range(start, end))
            elif remain[0] < cur_range[0] <= remain[-1] <= cur_range[-1]:
                nexto.append(range(remain[0], cur_range[0]))
                end = dest + remain[-1] - cur_range[0] + 1
                result.append(range(dest, end))
        remaining = nexto
    return result + remaining


with open(FILE_NAME, 'r') as file:
    for line in file:
        value = line.strip().split()
        if value:
            if seed_line:
                seeds = list(map(int, value[1:]))
                seed_line = False
            else:
                if value[0].isnumeric():
                    value = list(map(int, value))
                    mappings[current_key].append((range(value[1], value[1] + value[2]), value[0]))

                else:
                    current_key = value[0]


locations = [determine_location(seed, mappings, keymap) for seed in seeds]
res1 = min(locations)
print(res1)

seeds_chunks = [seeds[i:i + 2] for i in range(0, len(seeds), 2)]
seed_ranges = [range(start, start + length) for (start, length) in seeds_chunks]
ranges = determine_location_ranges(seed_ranges, mappings, keymap)
res2 = min(ranges, key=lambda x: x[0])[0]
print(res2)




