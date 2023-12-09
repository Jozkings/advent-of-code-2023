from typing import List

FILE_NAME = 'input9.in'

res1 = 0
res2 = 0


def is_end(history: List[int]) -> bool:
    return history[0] == 0 and len(set(history)) == 1


with open(FILE_NAME, 'r') as file:
    for index, line in enumerate(file):
        value = line.strip().split()
        current_history = list(map(int, value))
        predictions = [current_history]
        while not is_end(current_history):
            diffs = [current_history[i] - current_history[i-1] for i in range(1, len(current_history))]
            predictions.append(diffs)
            current_history = diffs

        predictions = predictions[::-1]
        predictions[0].append(0)
        predictions[0].insert(0, 0)

        for i in range(1, len(predictions)):
            predictions[i].append(predictions[i-1][-1] + predictions[i][-1])
            predictions[i].insert(0,  predictions[i][0] - predictions[i-1][0])

        res1 += predictions[-1][-1]
        res2 += predictions[-1][0]


print(res1)
print(res2)
