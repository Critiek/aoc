games = []

minimum_num_cubes = {
    'red': 0,
    'green': 0,
    'blue': 0,
}

with open('./input.txt', 'r') as file:
    for game in file:
        games.append(game.strip())

for game in games:
    print('')
    game = game.split()[2:]
    game = ''.join(game).split(';')
    for round in game:
        red_cubes, green_cubes, blue_cubes = [], [], []
        round = round.split(',')
        print(round)
        for draw in round:
            if draw[1].isnumeric():
                number_of_cubes = draw[0], draw[1] 
                number_of_cubes = ''.join(number_of_cubes)
            else:
                number_of_cubes = draw[0]
                
            minimum_num_cubes
