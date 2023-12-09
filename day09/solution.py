from collections import Counter, defaultdict, deque
import itertools as it
import more_itertools as mit
import functools as func
import operator as op
import networkx as nx
import math
import re

def p(v):
    print(v)
    return v

with open("input") as f:
    data = f.read().splitlines()


histories = [ list(map(int, line.split())) for line in data ]
part_1 = 0
part_2 = 0

for h in histories:
    rows = [ h ]
    while any(rows[-1]):
        rows.append([ b-a for a, b in it.pairwise(rows[-1]) ])
    next_value = 0
    prev_value = 0
    for row in rows[::-1]:
        next_value = row[-1] + next_value
        prev_value = row[0] - prev_value
    part_1 += next_value
    part_2 += prev_value


print(part_1)
print(part_2)
