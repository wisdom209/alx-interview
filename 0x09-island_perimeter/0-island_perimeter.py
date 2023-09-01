#!/usr/bin/python3
'''0x09. Island Perimeter'''


def calculate_consecutive_len(my_list, item):
    """get count of highest consecutive items in list"""
    counts = []
    counter = 0
    for x in my_list:
        if x == item:
            counter += 1
        else:
            counts.append(counter)
            counter = 0
    if len(counts) > 0:
        return max(counts)
    return 0


def island_perimeter(grid):
    '''returns the perimeter of the island described in grid'''
    gridlen = len(grid)
    inverse_grid = list(zip(*grid))

    if gridlen > 0:
        width_path = [0 for _ in grid[0]]
        height_path = [0 for _ in inverse_grid[0]]
        width = 0
        height = 0

        # get the width of island
        for row in grid:
            for index, cell in enumerate(row):
                if cell == 1:
                    width_path[index] = 1

        width = calculate_consecutive_len(width_path, 1)

        # get the height of island
        for row in inverse_grid:
            for index, cell in enumerate(row):
                if cell == 1:
                    height_path[index] = 1

        height = calculate_consecutive_len(height_path, 1)

        perimeter = (width + height) * 2
        return perimeter
