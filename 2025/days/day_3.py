# imports

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

# batteries is list of each battery bank line as a string

def part_1(batteries):
    answer = 0

    # for each bank
    for bank in batteries:
        first = 0
        first_index = 0
        second = 0

        # loop through for first battery
        for i, char in enumerate(bank):
            # if current battery is larger than what we have, replace
            # only go until second last index, so we have one battery left for second
            if (int(char) > first) and (i < len(bank) - 1):             
                first = int(char)
                first_index = i     # keep index of first battery to start second search from

        # now loop from first battery index to find best second battery
        for i in range(first_index + 1, len(bank)):
            if int(bank[i]) > second:
                second = int(bank[i])

        # combine first and second into a number and add to answer
        answer = answer + (int(str(first) + str(second)))
        
    return answer

#############################################################################################################

"""
For first one, as long as there's 11 left its fine to keep looking for the larget one
For second, as long as there's 10 left
etc
"""

def part_2(batteries):

    answer = 0

    for bank in batteries:

        # keep indexes and batteries(digits) to use
        indexes = [-1] * 12
        digits = [0] * 12
        length = 12

        # for each digit (battery) in the bank
        for i in range(12):
            # loop through from between previous index until how many we need left to find the largest
            for j in range(indexes[i - 1] + 1, (len(bank) - length) + 1):
                # if we found a larger one
                if int(bank[j]) > digits[i]:
                    digits[i] = int(bank[j])    # replace the digit
                    indexes[i] = j              # replace the index

            # decrease length left to search
            length = length - 1

        # combine the digits
        answer = answer + int("".join(map(str, digits)))

        
    return answer


##############################################################################################################

# Answer
batteries = get_input(INPUT)
print("Part 1:", part_1(batteries))
print("Part 2:", part_2(batteries))