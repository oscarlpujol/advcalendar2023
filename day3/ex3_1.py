# Used to import aux_tools
import sys
sys.path.append('..')
from aux_tools import file2arra

values = file2arra.file2array('./input.txt')

symbols = []

for row_num, row in enumerate(values):
    for char_num, character in enumerate(row):
        if not (character.isnumeric() or character == '.'):
            for length in (-1,0,1):
                for width in (-1,0,1):
                    symbols.append((row_num - length, char_num - width))

total = 0

number = 0

symbol_flag = False

for row_num, row in enumerate(values):
    for char_num, character in enumerate(row):
        if character.isnumeric():
            number = number*10 + int(character)
            if (row_num, char_num) in symbols:
                symbol_flag = True
        if char_num == len(row) - 1 or not character.isnumeric():
            if symbol_flag:
                total += number
                number = 0
                symbol_flag = False
            else:
                number = 0

print(total)