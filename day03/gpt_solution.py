def sum_part_numbers_based_on_user_code(schematic):
    """Sum all the part numbers in the engine schematic based on user's code logic."""
    grid = [list(line.strip()) for line in schematic]  # Convert to 2D grid
    sum_of_parts = 0

    # Creating a grid to mark adjacent symbols
    adjacent = [[False for _ in line] for line in grid]

    # Marking cells adjacent to symbols
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if not c.isdigit() and not c == ".":
                for k in range(max(0, i - 1), min(len(grid), i + 2)):
                    for l in range(max(0, j - 1), min(len(grid[0]), j + 2)):
                        adjacent[k][l] = True

    # Extracting numbers and checking adjacency
    for i, line in enumerate(grid):
        num = ""
        is_adjacent = False
        for j, c in enumerate(line):
            if c.isdigit():
                num += c
                is_adjacent |= adjacent[i][j]
            elif num != "":
                if is_adjacent:
                    sum_of_parts += int(num)
                is_adjacent = False
                num = ""
        if is_adjacent:
            sum_of_parts += int(num)

    return sum_of_parts


def find_gear_ratios(schematic):
    """Find and sum the gear ratios in the engine schematic."""
    grid = [list(line.strip()) for line in schematic]  # Convert to 2D grid
    total_gear_ratio = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '*':
                adjacent_numbers = []

                # Check all 8 adjacent positions for part numbers
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx == 0 and dy == 0:
                            continue  # Skip the current position
                        x, y = i + dx, j + dy
                        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y].isdigit():
                            number = ""
                            # Extract the full number horizontally
                            if 0 < y < len(grid[0]) - 1 and grid[x][y - 1].isdigit() and grid[x][y + 1].isdigit():
                                continue  # Middle of a number, skip
                            elif grid[x][y - 1].isdigit():  # Number starts from the left
                                ny = y
                                while ny >= 0 and grid[x][ny].isdigit():
                                    number = grid[x][ny] + number
                                    ny -= 1
                            else:  # Number starts from the current position
                                ny = y
                                while ny < len(grid[0]) and grid[x][ny].isdigit():
                                    number += grid[x][ny]
                                    ny += 1
                            if number and int(number) not in adjacent_numbers:
                                adjacent_numbers.append(int(number))

                # Calculate gear ratio if there are exactly two adjacent numbers
                if len(adjacent_numbers) == 2:
                    total_gear_ratio += adjacent_numbers[0] * adjacent_numbers[1]

    return total_gear_ratio

with open("input") as file:
    data = file.read().splitlines()
    print(sum_part_numbers_based_on_user_code(data))
    print(find_gear_ratios(data))
