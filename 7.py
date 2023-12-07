from functools import cmp_to_key
from typing import List, Tuple

FILE_NAME = 'input7.in'

res1 = 0
res2 = 0

mappings = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}


def open_list_two_columns(file_name: str) -> List[Tuple[str, str]]:
    with open(file_name, 'r') as file:
        return [tuple(line.strip().split()) for line in file]


def compare(first: Tuple[str, str], second: Tuple[str, str], remove_jacks: bool = False) -> int:
    f, s = first[0], second[0]
    first_count, second_count = [], []
    f_jacks_count, s_jacks_count = 0, 0

    if remove_jacks:
        f_jacks_count, s_jacks_count = f.count("J"), s.count("J")
        f, s = f.replace("J", ""), s.replace("J", "")

    first_count += sorted([f.count(x) for x in set(f)], reverse=True)
    second_count += sorted([s.count(x) for x in set(s)], reverse=True)

    if not first_count:
        first_count = [0]
    if not second_count:
        second_count = [0]

    first_count[0] += f_jacks_count
    second_count[0] += s_jacks_count

    if first_count > second_count:
        return 1
    if first_count < second_count:
        return -1
    return 1 if [mappings[x] for x in first[0]] >= [mappings[x] for x in second[0]] else -1


def first_compare(first: Tuple[str, str], second: Tuple[str, str]) -> int:
    return compare(first, second)


def second_compare(first: Tuple[str, str], second: Tuple[str, str]) -> int:
    return compare(first, second, remove_jacks=True)


hands = open_list_two_columns(FILE_NAME)
first_sort = sorted(hands, key=cmp_to_key(compare))
res1 = sum([(i + 1) * int(val[1]) for i, val in enumerate(first_sort)])
print(res1)

mappings["J"] = 1
second_sort = sorted(hands, key=cmp_to_key(second_compare))
res2 = sum([(i + 1) * int(val[1]) for i, val in enumerate(second_sort)])
print(res2)
