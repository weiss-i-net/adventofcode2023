from collections import Counter, defaultdict, deque
import itertools as it
import more_itertools as it
import functools as func
import operator as op
import math
import re

with open("input") as f:
    data = f.read().splitlines()

adjacent = [ [ False ] * len(data[0]) for _ in data ]
adjacent_star = [ [ False ] * len(data[0]) for _ in data ]
adjacent_number = [ [ 0 ] * len(data[0]) for _ in data ]


for i, line in enumerate(data):
    for j, c in enumerate(line):
        if not c.isdigit() and not c == ".":
            for k in range(max(0, i-1), min(len(data), i+2)):
                for l in range(max(0, j-1), min(len(data), j+2)):
                    adjacent[k][l] = True
                    if c == "*":
                        adjacent_star[k][l] = (i, j)

part_1 = 0
part_2 = 0

for i, line in enumerate(data):
    num = ""
    is_adjencent = False
    has_adjacent_star = False
    for j, c in enumerate(line):
        if c.isdigit():
            num += c
            is_adjencent |= adjacent[i][j]
            if adjacent_star[i][j]:
                has_adjacent_star = adjacent_star[i][j]
        elif num != "":
            if is_adjencent:
                part_1 += int(num)
            if has_adjacent_star:
                star_i, star_j = has_adjacent_star
                if not adjacent_number[star_i][star_j]:
                    adjacent_number[star_i][star_j] = int(num)
                else:
                    part_2 += adjacent_number[star_i][star_j] * int(num)

            is_adjencent = False
            has_adjacent_star = False
            num = ""

    if is_adjencent:
        part_1 += int(num)
    if has_adjacent_star:
        star_i, star_j = has_adjacent_star
        if not adjacent_number[star_i][star_j]:
            adjacent_number[star_i][star_j] = int(num)
        else:
            part_2 += adjacent_number[star_i][star_j] * int(num)


print(part_1)
print(part_2)
