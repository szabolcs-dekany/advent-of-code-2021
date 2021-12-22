from utils import read_directions


def run_part_one():
    print("--------------------------------")
    print("Advent of Code 2021 - 2 - Part 1")
    directions = read_directions()
    horizontal_position = 0
    depth = 0

    for x in range(len(directions)):
        if directions[x][0] == 'forward':
            horizontal_position += directions[x][1]
        if directions[x][0] == 'down':
            depth += directions[x][1]
        if directions[x][0] == 'up':
            depth -= directions[x][1]

    print('Horizontal position: {0}, Depth: {1}'.format(horizontal_position, depth))
    print('Final position: {0}'.format(horizontal_position * depth))
