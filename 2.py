FILE_NAME = 'input2.in'

res1 = 0  # first part
res2 = 0  # second part

MAX_BLUE = 14
MAX_RED = 12
MAX_GREEN = 13

with open(FILE_NAME, 'r') as file:
    for index, line in enumerate(file):
        game_index = index + 1
        value = line.strip().split()[2:]
        mino_red, mino_blue, mino_green = 0, 0, 0
        possible_game = True
        for i in range(0, len(value), 2):
            numo = int(value[i])
            color = value[i + 1].replace(',', '').replace(';', '')
            if color == 'blue':
                mino_blue = max(mino_blue, numo)
                possible_game = possible_game and (numo <= MAX_BLUE)
            elif color == 'red':
                mino_red = max(mino_red, numo)
                possible_game = possible_game and (numo <= MAX_RED)
            elif color == 'green':
                mino_green = max(mino_green, numo)
                possible_game = possible_game and (numo <= MAX_GREEN)
        power = mino_red * mino_blue * mino_green
        res1 += game_index * possible_game
        res2 += power


print(res1)
print(res2)
