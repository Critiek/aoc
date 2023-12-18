games = []

possible_games = []

red_cubes, green_cubes, blue_cubes = [], [], []

cubes = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

with open('./input.txt', 'r') as file:
    for game in file:
        games.append(game.strip())

def get_game_id(game):
    game = game.split()
    return int(game[1].replace(':', ''))

for game in games:
    game_possibility = True
    game_id = get_game_id(game)
    game = game.split()[2:]
    game = ''.join(game).split(';')
    # print('\nID:', game_id, game)
    for round in game:
        red_cubes, green_cubes, blue_cubes = [], [], []
        round = round.split(',')
        # print(round)
        for draw in round:
            if draw[1].isnumeric():
                number_of_cubes = draw[0], draw[1] 
                number_of_cubes = ''.join(number_of_cubes)
            else:
                number_of_cubes = draw[0]
            draw = ''.join([char for char in draw if not char.isnumeric()])
            # print(draw + ': ' + number_of_cubes)
            if draw == 'red':
                red_cubes.append(int(number_of_cubes))
            elif draw == 'green':
                green_cubes.append(int(number_of_cubes))
            elif draw == 'blue':
                blue_cubes.append(int(number_of_cubes))
        if sum(red_cubes) > cubes['red']:
            game_possibility = False
        elif sum(green_cubes) > cubes['green']:
            game_possibility = False
        elif sum(blue_cubes) > cubes['blue']:
            game_possibility = False
    # print(game_possibility)
    print('ID:', game_id, '   possibility:', game_possibility)
    if game_possibility:
        possible_games.append(game_id)
# print(possible_games)
print('\nSum of possible game IDs:', sum(possible_games))
