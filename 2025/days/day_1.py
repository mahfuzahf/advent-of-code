# Imports
import math


# Constants
LEFT = 'L'
RIGHT = 'R'
INPUT = '2025/resources/day_1_input.txt'


# Puzzle 1
def puzzle_1(filename):
    # variables to keep track of answer and arrow
    left_at_zero = 0
    arrow = 50

    with open (filename, 'r') as f:
        for line in f:
            # get rotation and direction
            rotation = int(line.strip('LR'))
            direction = line[0]

            # if right add, if left take away
            if direction == RIGHT:
                arrow = (arrow + rotation) % 100
                # if we land on 0, add to counter
                if arrow == 0:
                        left_at_zero += 1

            else:
                arrow = (arrow - rotation) % 100
                # if we land on 0, add to counter
                if arrow == 0:
                        left_at_zero += 1

    return left_at_zero


# Puzzle 2
def puzzle_2(filename):
    # variables to keep track of answer and arrow
    passed_zero = 0
    arrow = 50

    with open (filename, 'r') as f:
        for line in f:
            # get rotation and direction
            rotation = int(line.strip('LR'))
            direction = line[0]

            # get how many times it goes round
            rounds = math.trunc(rotation / 100)     # times it goes fully round dial
            rem = rotation % 100                    # clicks to go round after doing whole rounds

            # add whole rounds
            passed_zero = passed_zero + rounds

            # if arrow + rem mod 100 is larger than arrow, then its gone past 0 so add to m
            if direction == RIGHT:
                # if we add the remainder and its smaller, then we've passed 0
                if (((arrow + rem) % 100) < arrow):
                        passed_zero += 1

                # update the arrow
                arrow = (arrow + rotation) % 100

            else:
                # if we take away the remainder and the current number is larger than ther arrow, we have passed 1
                if (((arrow - rem) % 100) > arrow) and (arrow != 0):
                    passed_zero += 1

                # edge case: if we end up landing on 0 we also increment answer
                if (arrow - rem) == 0:
                    passed_zero += 1

                #update the arrow
                arrow = (arrow - rotation) % 100

    return passed_zero


# Answer
print(f"Answer to Puzzle 1: {puzzle_1(INPUT)}")
print(f"Answer to Puzzle 2: {puzzle_2(INPUT)}")



