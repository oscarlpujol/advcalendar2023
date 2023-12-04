# Used to import aux_tools
import sys
sys.path.append('..')
from aux_tools import file2arra

values = file2arra.file2array('./input.txt')

total_cards = 0

array_num = [0] * len(values)

for game_num, card in enumerate(values):
    card_numbers = card.split(':')[1]
    winning_numbers = card_numbers.split('|')[0].split(' ')
    dealt_numbers = card_numbers.split('|')[1].split(' ')
    numbers_matched = 0
    duplicated_cards_index = game_num
    for number in dealt_numbers:
        if number and number in winning_numbers:
            duplicated_cards_index += 1 
            array_num[duplicated_cards_index] += (array_num[game_num] + 1)

for duplicated_cards in array_num:
    total_cards += duplicated_cards + 1

print(total_cards)