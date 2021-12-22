from utils import read_directions


def run_part_two():
    print("--------------------------------")
    print("Advent of Code 2021 - 2 - Part 2")
    directions = read_directions()
    horizontal_position = 0
    depth = 0
    aim = 0

    for x in range(len(directions)):
        if directions[x][0] == 'forward':
            horizontal_position += directions[x][1]
            depth = depth + (aim * directions[x][1])
        if directions[x][0] == 'down':
            aim += directions[x][1]
        if directions[x][0] == 'up':
            aim -= directions[x][1]

    print('Horizontal position: {0}, Depth: {1}, Aim: {2}'.format(horizontal_position, depth, aim))
    print('Final position: {0}'.format(horizontal_position * depth))
