# imports

# Constants
INPUT = '2025/resources/day_5_input.txt'
TEST = '2025/resources/day_5_test.txt'
TESTRANGE = '2025/resources/day_5_test_range.txt'
TESTID = '2025/resources/day_5_test_id.txt'
INPUTRANGE = '2025/resources/day_5_input_range.txt'
INPUTID = '2025/resources/day_5_input_id.txt'

#############################################################################################################

# merge ranges
def merge_ranges(ranges):
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


# get our input
def get_input(filename_range, filename_id):

    # read the file
    with open (filename_range, 'r') as f:
        ranges_string = f.read().splitlines()

    with open (filename_id, 'r') as f:
        ids_string = f.read().splitlines()

    # split ranges up
    ranges = []
    for item in ranges_string:
        numbers = item.split('-') 
        lower = int(numbers[0])
        higher = int(numbers[1])
        ranges.append([lower, higher])

    # now sort and merge them
    ranges = merge_ranges(ranges)

    ids = [int(item) for item in ids_string]

    # return data
    return ranges, ids


#############################################################################################################

def part_1(ranges, ids):
    answer = 0
    
    # loop through each id and check
    for id in ids:
        for r in ranges:
            if (r[0] <= id <= r[1]):
                answer += 1
                break

    return answer

#############################################################################################################

def part_2(ranges):
    answer = 0

    for r in ranges:
        answer = answer + ((r[1] + 1) - r[0])

    return answer

#############################################################################################################

ranges, ids = get_input(INPUTRANGE, INPUTID)

print(f"Answer to Part 1: {part_1(ranges, ids)}")
print(f"Answer to Part 2: {part_2(ranges)}")