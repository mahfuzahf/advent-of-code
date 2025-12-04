# imports
import re
import math
import random

# Constants
INPUT = '2025/resources/day_4_input.txt'
TEST = '2025/resources/day_4_test.txt'

#############################################################################################################

# get our input
def get_input(filename):
    
    grid = []

    # read the file
    with open (filename, 'r') as f:
        data = f.read().splitlines()

    # split each character up in the row
    for row in data:
        grid.append(list(row))


    # return data
    return grid

#############################################################################################################

grid = get_input(INPUT)

#############################################################################################################

# get a list of neighbours
def get_neighbours(grid, i, j):

    width = len(grid[0])
    height = len(grid)
    neighbours = []

    """
    Go up then left then do next 3 along
    Go down then left and do next 3 along
    left
    right
    """

    # # go through each row and cell
    # for j, row in enumerate(grid):
    #     for i, cell in enumerate(row):

    # find what the neighbours are
    # left
    if i - 1 >= 0:
        neighbours.append(grid[j][i - 1])

    # right
    if i + 1 < width:
        neighbours.append(grid[j][i + 1])

    # up
    # check we can even go up
    if (j - 1) >= 0:
        # normal case
        if ((i - 1) >= 0) and ((i + 1) < width):
            for k in range(3):
                neighbours.append(grid[j - 1][i - 1 + k])

        # left side
        if ((i - 1) < 0) and ((i + 1) < width):
            for k in range(2):
                neighbours.append(grid[j - 1][i + k])

        # right side
        if ((i - 1) >= 0) and ((i + 1) >= width):
            for k in range(2):
                neighbours.append(grid[j - 1][i - k])

    # down
    # check we can even go down
    if (j + 1) < height:
        # normal case
        if ((i - 1) >= 0) and ((i + 1) < width):
            for k in range(3):
                neighbours.append(grid[j + 1][i - 1 + k])

        # left side
        if ((i - 1) < 0) and ((i + 1) < width):
            for k in range(2):
                neighbours.append(grid[j + 1][i + k])

        # right side
        if ((i - 1) >= 0) and ((i + 1) >= width):
            for k in range(2):
                neighbours.append(grid[j + 1][i - k])

    return neighbours



# answer = 0
# coords = []

# # go through each row and cell
# for j, row in enumerate(grid):
#     for i, cell in enumerate(row):
#         # check if its a roll
#         if cell == '@':
#             # find what the neighbours are
#             neighbours = get_neighbours(grid, i, j)
#             count = neighbours.count('@')
#             if count < 4:
#                 answer = answer + 1
#                 coords.append((i, j))

# print(answer)

# # for coord in coords:
# #     grid[coord[1]][coord[0]] = 'x'

# # for row in grid:
# #     print(''.join(row))


answer = 0
coords = []

updated = -1

while updated != 0:
    updated = 0
    # go through each row and cell
    for j, row in enumerate(grid):
        for i, cell in enumerate(row):
            # check if its a roll
            if cell == '@':
                # find what the neighbours are
                neighbours = get_neighbours(grid, i, j)
                count = neighbours.count('@')
                if count < 4:
                    answer = answer + 1
                    grid[j][i] = 'x'
                    coords.append((i, j))
                    updated += 1

print(answer)

# for coord in coords:
#     grid[coord[1]][coord[0]] = 'x'

# for row in grid:
#     print(''.join(row))


