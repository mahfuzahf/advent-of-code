# imports

# Constants
INPUT = '2025/resources/day_4_input.txt'
TEST = '2025/resources/day_4_test.txt'

#############################################################################################################

# get our input into 2D list
def file_to_grid(filename):
    
    grid = []

    # read the file
    with open (filename, 'r') as f:
        data = f.read().splitlines()

    # split each character up in the row
    for row in data:
        grid.append(list(row))


    # return data
    return grid


# get a list of neighbours
def get_neighbours(grid, i, j):

    width = len(grid[0])
    height = len(grid)
    neighbours = []

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
        # normal case - do 3 along from left
        if ((i - 1) >= 0) and ((i + 1) < width):
            for k in range(3):
                neighbours.append(grid[j - 1][i - 1 + k])

        # left side - do 2 along from top
        if ((i - 1) < 0) and ((i + 1) < width):
            for k in range(2):
                neighbours.append(grid[j - 1][i + k])

        # right side - do 2 along backwards from top
        if ((i - 1) >= 0) and ((i + 1) >= width):
            for k in range(2):
                neighbours.append(grid[j - 1][i - k])

    # down
    # check we can even go down
    if (j + 1) < height:
        # normal case - do 3 along from left
        if ((i - 1) >= 0) and ((i + 1) < width):
            for k in range(3):
                neighbours.append(grid[j + 1][i - 1 + k])

        # left side - do 2 along from top
        if ((i - 1) < 0) and ((i + 1) < width):
            for k in range(2):
                neighbours.append(grid[j + 1][i + k])

        # right side - do 2 along backwards from top
        if ((i - 1) >= 0) and ((i + 1) >= width):
            for k in range(2):
                neighbours.append(grid[j + 1][i - k])

    return neighbours

#############################################################################################################

def part_1(grid, to_print=False):

    answer = 0
    coords = []

    # go through each row and cell
    for j, row in enumerate(grid):
        for i, cell in enumerate(row):
            # check if its a roll
            if cell == '@':
                # find what the neighbours are
                neighbours = get_neighbours(grid, i, j)
                count = neighbours.count('@')           # count neighbouring rolls
                if count < 4:                           # if less than 4, its accessible
                    answer = answer + 1
                    coords.append((i, j))

    # can print to check
    if to_print:
        # replace the accessible rows
        for coord in coords:
            grid[coord[1]][coord[0]] = 'x'

        for row in grid:
            print(''.join(row))

    return answer


def part_2(grid):

    answer = 0
    coords = []

    # to check if any rolls have been removed in the current pass
    updated = True

    # while rolls have been removed (need to do a last pass to check all have been removed)
    while updated:
        updated = False             # reset updated     
        # go through each row and cell
        for j, row in enumerate(grid):
            for i, cell in enumerate(row):
                # check if its a roll
                if cell == '@':
                    # find what the neighbours are
                    neighbours = get_neighbours(grid, i, j)
                    count = neighbours.count('@')           # count neighbouring rolls
                    if count < 4:                           # if its accessible, remove it
                        answer = answer + 1
                        grid[j][i] = 'x'                    # denote removed as x   
                        coords.append((i, j))
                        updated = True                      # flip updated

    return answer

#############################################################################################################

# Answers
grid = file_to_grid(INPUT)
print("Part 1:", part_1(grid))
print("Part 2:", part_2(grid))