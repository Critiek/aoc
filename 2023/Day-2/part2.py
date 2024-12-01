games = []

with open('./input.txt', 'r') as file:
    for game in file:
        games.append(game.strip())

for game in games:
    print('')
    game = game.split()[2:]
    game = ''.join(game).split(';')
    for round in game:
        minimum_red_cubes, minimum_green_cubes, minimum_blue_cubes = [], [], []
        round = round.split(',')
        print(round)
        for draw in round:
            if draw[1].isnumeric():
                number_of_cubes = draw[0], draw[1] 
                number_of_cubes = ''.join(number_of_cubes)
            else:
                number_of_cubes = draw[0]
                
            print(number_of_cubes)
