import sys


class Grid:
    def __init__(self, input):
        self.data = list(map(list, input.splitlines()))
        self.N = len(self.data)
        self.M = len(self.data[0])

    def get_elem(self, i, j, direction):
        if direction % 2 == 0:
            return self.data[i][j]
        else:
            return self.data[j][i]

    def set_elem(self, i, j, direction, val):
        if direction % 2 == 0:
            self.data[i][j] = val
        else:
            self.data[j][i] = val

    def __str__(self):
        return "\n".join("".join(line) for line in self.data)


def down_delta(d):
    if d in (0, 1):
        return 1
    else:
        return -1


def get_north_load(grid):
    return sum(
        grid.N - i for i, row in enumerate(grid.data) for cell in row if cell == "O"
    )


def tilt(grid, direction):
    col_index = {
        0: range(grid.M),  # north
        1: range(grid.N - 1, -1, -1),  # west
        2: range(grid.M - 1, -1, -1),  # south
        3: range(grid.N),  # east
    }
    row_index = {
        0: range(grid.N),
        1: range(grid.M),
        2: range(grid.N - 1, -1, -1),
        3: range(grid.M - 1, -1, -1),
    }
    for col in col_index[direction]:
        support = row_index[direction].start

        for row in row_index[direction]:
            cell = grid.get_elem(row, col, direction)
            if cell == "O":
                grid.set_elem(row, col, direction, ".")
                grid.set_elem(support, col, direction, "O")
                support += down_delta(direction)
            if cell == "#":
                support = row
                support += down_delta(direction)


grid = Grid(sys.stdin.read())

tilt(grid, 0)
print("Part 1:", get_north_load(grid))

cycles_done = 0
cycles_left = 1000000000
reduced = False
seen = dict()
while cycles_left:
    if not reduced:
        key = str(grid)
        if key in seen:
            cycles_left %= cycles_done - seen[key]
            reduced = True
        seen[key] = cycles_done

    for direction in range(4):
        tilt(grid, direction)

    cycles_done += 1
    cycles_left -= 1

print("Part 2:", get_north_load(grid))
