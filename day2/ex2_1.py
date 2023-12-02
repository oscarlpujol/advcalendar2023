# Used to import aux_tools
import sys
sys.path.append('..')
from aux_tools import file2arra

values = file2arra.file2array('./input.txt')

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

balls_dict = {
    "blue" : MAX_BLUE,
    "green" : MAX_GREEN,
    "red" : MAX_RED
}

total = 0

for game in values:
    winned_round = True
    splited_games = game.split(': ')
    game_id = int(splited_games[0].split(' ')[1])
    rounds = splited_games[1].split('; ')
    for game_round in rounds:
        balls = game_round.split(', ')
        for ball in balls:
            number = int(ball.split(' ')[0])
            colour = ball.split(' ')[1]
            if number > balls_dict[colour]:
                winned_round = False

    if winned_round:
        total += game_id

print(total)