import os
file_path = os.path.join('Advent of Code 2023','day2.txt')
with open(file_path, 'r') as f:
    lines = f.readlines()
    games = [entry.strip() for entry in lines]


''' # Part 1
game_count = []

for item in games:
    game_info = item.split(':')[-1].split(';')
    game_number = item.split()[1]
    is_valid = True

    for idx, game_set in enumerate(game_info):
        colours = {'blue': 0, 'red': 0 , 'green': 0}
        colour_list = game_set.split(',')

        for colour in colour_list:
            count, col = colour.strip().split()
            colours[col] += int(count)

        if colours['red'] > 12 or colours['blue'] > 14 or colours['green'] > 13:
            is_valid = False
            break
    if is_valid:
        game_count.append(int(game_number.strip(':')))

print(sum(game_count))'''

# Part 2

game_colours = {}

for item in games:
    game_info = item.split(':')[-1].split(';')
    game_number = item.split()[1]
    game_colours[game_number.strip(':')] = {'blue': 0, 'red': 0 , 'green': 0}

    for idx, game_set in enumerate(game_info):
        colours = {'blue': 0, 'red': 0 , 'green': 0}
        colour_list = game_set.split(',')

        for colour in colour_list:
            count, col = colour.strip().split()
            colours[col] += int(count)
        
        for colour, count in colours.items():
            game_colours[game_number.strip(':')][colour] = max(game_colours[game_number.strip(':')][colour], count)

game_products = {}

for game, colours in game_colours.items():
    product = 1
    for count in colours.values():
        product *= count
    game_products[game] = product

total_sum = sum(game_products.values())
print(total_sum)