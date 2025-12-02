# imports
import re
from sympy import factorint
import math

# Constants
INPUT = '2025/resources/day_2_input.txt'
TEST = '2025/resources/day_2_test.txt'

#############################################################################################################

# get our input
def get_input(filename):

    # get our numbers
    range_list = []

    # read the file
    with open (filename, 'r') as f:
        # convert to list
        temp_range_list = f.read().split(",")

        # for each item in list, split into tuple of first and last
        for item in temp_range_list:
            numbers = item.split('-')                               # list of two numbers as string
            range_list.append((int(numbers[0]), int(numbers[1])))   # add them as tuples

    return range_list

#############################################################################################################

"""ok well if there are repeating numbers then the number has an even number of digits
   so we can split into two and see if the two halves are the same """

def part_1(range_list):
    # store answer
    answer = 0

    # for each range
    for range_boundaries in range_list:
        lower, higher = range_boundaries        # get the boundaries

        # for each number in the range
        for i in range(lower, higher + 1):
            string_id = str(i)                  # convert the number to a sting 
            
            # if the length of a string is even
            if len(string_id) % 2 == 0:
                half = int(len(string_id)/2)    # get halfway point

                left = string_id[0:half]        # get the two halves
                right = string_id[half:]

                # if the halves are the same the ID is invalid
                if left == right:
                    # add the invalid ID to the answer
                    answer += i

    # part 1 = 29940924880
    return answer

#############################################################################################################
            
"""
We could brute force it, and try each number of characters as a sequence until we get two halves.
Not the fastest but oh well. 
"""
def part_2(range_list):
    # store answer
    answer = 0

    # for each range
    for range_boundaries in range_list:
        lower, higher = range_boundaries    # get the boundaries

        # for each number in the range
        for i in range(lower, higher + 1):
            string_id = str(i)                  # convert the number to a sting 
            id_len = len(string_id)             # get the length of the string

            # for each sequence of characters from 1 till halfway
            for j in range (1, (id_len // 2) + 1):

                # edge case: number is all the same digits
                num_same_digits = set(string_id)
                if len(num_same_digits) == 1:
                    answer += i                 # we add to the answer, then break from the loop so we don't keep adding it
                    break
                
                
                # if string not a multiple of this sequence length, pass
                if id_len % j != 0:
                    pass
                
                else:
                    # split the string up into lengths of the sequence
                    ref = '.' * j
                    # store as a set to see how many unique segments
                    spliced_id = set(re.findall(ref, string_id))

                    # if set is length 1 then the id is invalid
                    if len(spliced_id) == 1:
                        answer += i
                        break           # make sure you break from the loop

    return answer

#############################################################################################################

# Answer
input = get_input(INPUT)
print(f"Answer to Puzzle 1: {part_1(input)}")
print(f"Answer to Puzzle 2: {part_2(input)}")

