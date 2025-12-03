# imports
import re
import math
import random

# Constants
INPUT = '2025/resources/day_3_input.txt'
TEST = '2025/resources/day_3_test.txt'

#############################################################################################################

# get our input
def get_input(filename):

    # read the file
    with open (filename, 'r') as f:
        data = f.read().splitlines()

    # return data
    return data


#############################################################################################################

batteries = get_input(INPUT)

#############################################################################################################

# input is list of each line as a string
# convert to int

# answer = 0

# for bank in batteries:
#     first = 0
#     first_index = 0
#     second = 0
#     second_index = 0

#     # loop through
#     for i, char in enumerate(bank):
#         if (int(char) > first) and (i < len(bank) - 1):
#             first = int(char)
#             first_index = i

#     # now loop from first index
#     for i in range(first_index + 1, len(bank)):
#         if int(bank[i]) > second:
#             second = int(bank[i])
#             second_index = i

#     # combine first and second
#     # print(int(str(first) + str(second)))
#     answer = answer + (int(str(first) + str(second)))
    
# print(answer)

#############################################################################################################

"""
For first one, as long as there's 11 left its fine to keep looking for the larget one
For second, as long as there's 10 left
etc
"""

answer = 0

# 987654321111111
# 811111111111119
for bank in batteries:

    # keep indexes
    indexes = [-1] * 12
    digits = [0] * 12
    length = 12

    # for each digit
    for i in range(12):
        # loop through from between previous index until how many we need left to find the largest
        for j in range(indexes[i - 1] + 1, (len(bank) - length) + 1):
            # if we found a larger one
            if int(bank[j]) > digits[i]:
                digits[i] = int(bank[j])
                indexes[i] = j

        # decrease length
        length = length - 1

    # combine the digits
    answer = answer + int("".join(map(str, digits)))

    
print(answer)
