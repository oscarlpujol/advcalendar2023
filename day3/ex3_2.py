# Used to import aux_tools
import sys
sys.path.append('..')
from aux_tools import file2arra

values = file2arra.file2array('./input.txt')

symbols = []

for row_num, row in enumerate(values):
    for char_num, character in enumerate(row):
        if character == '*':
            symbols.append((row_num, char_num))

total = 0

number = 0
numbers = []
symbol_flag = True
num_obj = 0
count = 0

for symbol in symbols:
    value_start = symbol[0] - 1 if symbol[0] > 0 else symbol[0]
    value_end = (symbol[0] + 1 if symbol[0] < len(values[:]) - 1 else symbol[0]) + 1
    char_start = symbol[1] -1 if symbol[1] > 0 else symbol[1]
    char_end = symbol[1] + 1 if symbol[1] < len(values[:]) - 1 else symbol[1]
    for row_num, row in enumerate(values[value_start:value_end]):
        for char_num, character in enumerate(row):
            if character.isnumeric():
                number = number*10 + int(character)
                if char_num in [char_start, symbol[1], char_end]:
                    symbol_flag = True
            if char_num == len(row) - 1 or not character.isnumeric():
                if number != 0 and symbol_flag:
                    num_obj += 1
                    numbers.append(number)
                symbol_flag = False
                number = 0
    if num_obj == 2:
        total += numbers[0] * numbers[1]
    numbers = []
    num_obj = 0

print(total)