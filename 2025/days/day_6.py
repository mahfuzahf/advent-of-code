# imports
import operator
from functools import reduce

# Constants
INPUT = '2025/resources/day_6_input.txt'
TEST = '2025/resources/day_6_test.txt'

OPS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "%": operator.mod
}  

#############################################################################################################

def get_input(filename):

    # read the file
    with open (filename, 'r') as f:
        data = f.read().splitlines()

    # for each line, split by whitespaces
    line_numbers = []
    for i in range (len(data)):
        line_numbers.append(data[i].split())

    # split by operands and operators
    operands = line_numbers[0:len(line_numbers) - 1]
    operators = line_numbers[-1]

    # return data
    return operands, operators

def largest_in_column(filename):
    largests = []

    # read the file
    with open (filename, 'r') as f:
        data = f.read().splitlines()

    # for each line, split by whitespaces
    line_numbers = []
    for i in range (len(data) - 1):
        line_numbers.append(data[i].split())


    # transpose
    operands = [list(row) for row in zip(*line_numbers)]
    
    for column in operands:
        largests.append(len(max(column, key=len)))

    return largests



def get_input_2(filename):
    # read the file
    with open (filename, 'r') as f:
        data = f.read().splitlines()

    # for each line, split by whitespaces
    line_numbers = []
    for i in range (len(data) - 1):
        line_numbers.append(data[i].split(" "))

    operators = data[-1].split()

    operands = []

    largests = largest_in_column(filename)

    # for each line number, concatenate 0s 
    for i, line in enumerate(line_numbers):
        actual_line = []
        current_index = 0
        # for each number get the largest number in the column
        for c_len in largests:
            curr_len = 0
            line_chars = []

            # join up the 

            while curr_len < c_len:

                

                if len(line[current_index]) > 0:
                    for char in line[current_index]:
                        line_chars.append(char)
                        curr_len += 1
                    current_index += 1
                else:
                    line_chars.append(' ')    
                    current_index += 1
                    curr_len += 1

            actual_line.append(''.join(line_chars))

        operands.append(actual_line)

    # return data
    return operands, operators


#############################################################################################################

def part_1(operands, operators):
    answer = 0

    num_eq = len(operands[0])
    num_op = len(operands)

    # for each equation
    for i in range(num_eq):
        # get the operator
        operator = OPS[operators[i]]
        # get list of operands
        list_ops = [int(operands[j][i]) for j in range(num_op)]
        # do the maths
        eq_ans = reduce(operator, list_ops)
        answer += eq_ans

    return answer


#############################################################################################################

def part_2(operands, operators):
    answer = 0

    num_eq = len(operators)
    

    # for each equation
    for i in range(num_eq):
        # number of operands is the length of the largest operand in the column
        num_op = len(operands[0][i])
        # get the operator
        operator = OPS[operators[i]]
        # get list of operands
        list_ops = []
        for c in range(num_op):
            # get the numbers in the column
            column = [operands[j][i] for j in range(len(operands))]
            operand = [column[j][c] for j in range(len(operands))]
            list_ops.append(''.join(operand))

        actual_ops = [int(item) for item in  list_ops]


        # do the maths
        eq_ans = reduce(operator, actual_ops)
        answer += eq_ans

    return answer

#############################################################################################################

operands, operators = get_input_2(INPUT)


# print(part_1(operands, operators))
print(part_2(operands, operators))