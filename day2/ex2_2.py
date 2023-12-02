# Used to import aux_tools
import sys
sys.path.append('..')
from aux_tools import file2arra

values = file2arra.file2array('./input.txt')

total = 0

for game in values:
    splited_games = game.split(': ')
    rounds = splited_games[1].split('; ')
    min_balls = {
            "blue" : 0,
            "red" : 0,
            "green": 0
    }
    for game_round in rounds:
        balls = game_round.split(', ')
        for ball in balls:
            number = int(ball.split(' ')[0])
            colour = ball.split(' ')[1]
            if number > min_balls[colour]:
                min_balls[colour] = number

    game_total = 1

    for num_balls in min_balls.values():
        game_total *= num_balls
    total += game_total

print(total)