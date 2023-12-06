FILE_NAME = 'input6.in'

res1 = 1
res2 = 0

time_line = True


def get_winning_ways_number(time: int, distance: int) -> int:
    low_index, high_index = 0, time
    low_bound, high_bound = False, False

    while not (low_bound or high_bound):
        if not low_bound:
            speed = low_index
            current_time = time - speed
            my_distance = speed * current_time
            if my_distance > distance:
                low_bound = True
            else:
                low_index += 1
        if not high_bound:
            speed = high_index
            current_time = time - speed
            my_distance = speed * current_time
            if my_distance > distance:
                high_bound = True
            else:
                high_index -= 1

    return high_index - low_index + 1


with open(FILE_NAME, 'r') as file:
    for index, line in enumerate(file):
        value = line.strip().split()
        if time_line:
            time_line = False
            big_time = int(''.join(value[1:]))
            times = list(map(int, value[1:]))
        else:
            big_distance = int(''.join(value[1:]))
            distances = list(map(int, value[1:]))


for i in range(len(times)):
    time, distance = times[i], distances[i]
    res1 *= get_winning_ways_number(time, distance)

print(res1)

res2 = get_winning_ways_number(big_time, big_distance)
print(res2)
