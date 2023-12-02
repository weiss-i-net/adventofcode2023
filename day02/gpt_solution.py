# Advent of Code 2023 - Day 2: Cube Conundrum

def parse_game_data(game_line):
    # Parse a single line of game data and return the sets of cubes as a list of dictionaries
    _, game_data = game_line.split(': ')
    sets = game_data.strip().split('; ')
    cube_sets = []
    for set in sets:
        cubes = set.split(', ')
        cube_count = {}
        for cube in cubes:
            count, color = cube.split(' ')
            cube_count[color] = int(count)
        cube_sets.append(cube_count)
    return cube_sets

def is_game_possible(cube_sets, max_cubes):
    # Check if a game is possible with the given maximum cubes
    for set in cube_sets:
        for color, count in set.items():
            if count > max_cubes[color]:
                return False
    return True

def find_minimum_cubes(cube_sets):
    # Find the minimum number of cubes needed for each color for a game
    min_cubes = {'red': 0, 'green': 0, 'blue': 0}
    for set in cube_sets:
        for color, count in set.items():
            min_cubes[color] = max(min_cubes[color], count)
    return min_cubes

def calculate_power(cube_counts):
    # Calculate the power of a set of cubes, defined as the product of the counts of each color
    return cube_counts['red'] * cube_counts['green'] * cube_counts['blue']

def main(input_data):
    # Process the input data for both parts of the puzzle
    # Part 1: Sum of IDs of possible games
    max_cubes = {'red': 12, 'green': 13, 'blue': 14}
    possible_games_sum = 0

    # Part 2: Sum of the power of the minimum sets of cubes
    total_power_sum = 0

    for line in input_data:
        game_id_str, _ = line.split(':')
        game_id = int(game_id_str.split(' ')[1])
        cube_sets = parse_game_data(line)

        # Part 1
        if is_game_possible(cube_sets, max_cubes):
            possible_games_sum += game_id

        # Part 2
        min_cubes = find_minimum_cubes(cube_sets)
        power = calculate_power(min_cubes)
        total_power_sum += power

    return possible_games_sum, total_power_sum

# Read the input file
with open('input', 'r') as file:
    input_data = file.readlines()

# Run the main function
possible_games_sum, total_power_sum = main(input_data)
print(f"Sum of IDs of possible games: {possible_games_sum}")
print(f"Sum of the power of the minimum sets: {total_power_sum}")

