# file of (what I think are) useful functions I make during the course of AoC

def file_to_grid(filename):
    """
    Converts a file into a 2D list representing a grid. Assuming each line is a row, and each character in a row is a cell.
    
    :param filename: name of file with contents to be turned into grid. 
    :type filename: str

    :returns grid: A 2D list representing the grid.
    :rtype: 2D list.
    """
    
    grid = []

    # read the file
    with open (filename, 'r') as f:
        data = f.read().splitlines()

    # split each character up in the row
    for row in data:
        grid.append(list(row))


    # return data
    return grid


def get_neighbours(grid, i, j):
    """
    For a given grid, and co-ordinates (i, j), returns a list of neighbours. i is along the x axis and j down the y, so this assumes the grid is indexed grid[j][i].
    
    :param grid: 2D list representing the grid.
    :type grid: 2D list
    :param i: i coordinate going along the row
    :type i: int
    :param j: j coordinate going down the row
    :type j: int

    :returns neighbours: A list of contents of neighbours.
    :rtype: List
    """

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