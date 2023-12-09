from collections import Counter, defaultdict, deque
import itertools as it
import more_itertools as mit
import functools as func
import numpy as np
import operator as op
import networkx as nx
import math
import re

def p(v):
    print(v)
    return v

with open("input") as f:
    data = f.read().splitlines()

LR = data[0]
m = {}
for line in data[2:]:
    src, dst = line.split(" = ")
    l, r = dst[1:-1].split(", ")
    m[src] = (l, r)

loc = "AAA"
steps = 0
for inst in it.cycle(LR):
    if loc == "ZZZ":
        break
    loc = m[loc][0 if inst == "L" else 1]
    steps += 1
print("Part 1:", steps)

locs = tuple(node for node in m if node[2] == "A")
cycles = []
steps = 0

for l in locs:
    loc = l
    first_z = 0
    steps = 0
    for inst in it.cycle(LR):
        if loc[2] == "Z":
            if first_z:
                cycles.append(steps - first_z)
                break
            else:
                first_z = steps
        loc = m[loc][0 if inst == "L" else 1]
        steps += 1

print("Part 2:", np.lcm.reduce(cycles))

