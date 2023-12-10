import itertools as it
import sys

data = sys.stdin.read().splitlines()

empty_row = [ all(c == "." for c in row) for row in data ]
empty_col = [ all(c == "." for c in col) for col in zip(*data) ]

def solution(part):
    galaxies = []
    row_offset = 0
    for i, line in enumerate(data):
        col_offset = 0
        if empty_row[i]:
            row_offset += 1 if part == 1 else 999999
        for j, char in enumerate(line):
            if empty_row[j]:
                col_offset += 1 if part == 1 else 999999
            if char == "#":
                galaxies.append((i + row_offset, j + col_offset))

    return sum(abs(x-i)+abs(y-j) for (x, y), (i, j) in it.combinations(galaxies, 2))

print("Part 1:", solution(1))
print("Part 2:", solution(2))
