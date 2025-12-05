# file of (what I think are) useful functions I make during the course of AoC

def file_to_grid(filename):
    """
    Converts a file into a 2D list representing a grid. Assuming each line is a row, and each character in a row is a cell.
    
    :param filename: name of file with contents to be turned into grid. 
    :type filename: str

    :returns grid: A 2D list representing the grid.
    :rtype: 2D List
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


# merge ranges
def merge_ranges(ranges):
    """
    Given a list of ranges, and each range a list [lower, higher], will sort and merge as many ranges as it can.
    
    :param ranges: List of integer ranges.
    :type ranges: 2D List

    :returns merged_ranges: List of sorted and merged ranges.
    :rtype: 2D List
    """

    # sort ranges
    ranges = sorted(ranges)

    # convert to a massive range - initialise with first range in list
    merged_ranges = [ranges[0]]

    # keep track of our current range
    current_range = 0

    for i in range(1, len(ranges)):
        # if the lower value of the range is within the current range
        if ranges[i][0] <= merged_ranges[current_range][1]:
            # merge the range if the higher value is higher 
            if merged_ranges[current_range][1] < ranges[i][1]:
                merged_ranges[current_range][1] = ranges[i][1]

        else:
            # if not, have to make a separate range
            merged_ranges.append(ranges[i])
            current_range += 1

    return merged_ranges
