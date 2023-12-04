# Used to import aux_tools
import sys
sys.path.append('..')
from aux_tools import file2arra

values = file2arra.file2array('./input.txt')

total = 0

for card in values:
    card_numbers = card.split(':')[1]
    winning_numbers = card_numbers.split('|')[0].split(' ')
    dealt_numbers = card_numbers.split('|')[1].split(' ')
    numbers_matched = 0
    for number in dealt_numbers:
        if number and number in winning_numbers:
            numbers_matched += 1
    if numbers_matched != 0:
        total += 2 ** (numbers_matched - 1)

print(total)