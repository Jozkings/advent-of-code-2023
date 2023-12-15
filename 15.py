from collections import defaultdict as dd
from typing import List

FILE_NAME = 'input15.in'

res1 = 0
res2 = 0


def hash(value: str) -> int:
    res = 0
    for charo in value:
        res += ord(charo)
        res *= 17
        res %= 256
    return res


def box_equals(lenses: List[str], new_lens: str) -> List[str]:
    if not lenses:
        return [new_lens]
    replaced = False
    res = []
    label = new_lens.split("_")[0]
    for lens in lenses:
        if lens.split("_")[0] == label:
            res.append(new_lens)
            replaced = True
        else:
            res.append(lens)
    if not replaced:
        res.append(new_lens)
    return res


def box_dash(lenses: List[str], new_lens: str) -> List[str]:
    if not lenses:
        return []
    res = []
    label = new_lens.split("_")[0]
    for lens in lenses:
        if lens.split("_")[0] != label:
            res.append(lens)
    return res


data = [x for x in open(FILE_NAME).read().split(",")]
boxes = dd(list)

for value in data:
    res1 += hash(value)
    label, length = value.split("=" if "=" in value else '-')
    lens_str = '_'.join([label, length])
    label_hash = hash(label)
    function = box_equals if "=" in value else box_dash
    boxes[label_hash] = function(boxes[label_hash], lens_str)


for key, values in boxes.items():
    box_number = key + 1
    for index, val in enumerate(values):
        lens_number = index + 1
        focal_length = int(val.split("_")[1])
        res2 += (box_number * lens_number * focal_length)

print(res1)
print(res2)
