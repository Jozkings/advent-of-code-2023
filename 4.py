from collections import defaultdict as dd

FILE_NAME = 'input4.in'

res1 = 0
res2 = 0

counts = dd(int)


with open(FILE_NAME, 'r') as file:
    for index, line in enumerate(file):
        counts[index + 1] += 1
        value = line.strip().split(' ')[2:]
        my_numbers, winning_numbers = set(), set()
        current_numbers = set()
        current_reward = index + 2
        for val in value:
            if val == '|':
                winning_numbers = current_numbers
                current_numbers = set()
            elif val.strip().isnumeric():
                current_numbers.add(int(val.strip()))
        my_numbers = current_numbers
        my_winning_numbers = winning_numbers & my_numbers
        res1 += 0 if not my_winning_numbers else 2 ** (len(my_winning_numbers & my_numbers) - 1)

        for i in range(len(my_winning_numbers)):
            counts[current_reward + i] += counts[index + 1]

    res2 = sum(counts.values())

print(res1)
print(res2)
