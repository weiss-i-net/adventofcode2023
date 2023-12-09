from collections import Counter, defaultdict, deque
import itertools as it
import more_itertools as mit
import functools as func
import numpy as np
import operator as op
import networkx as nx
import math
import re
import sympy
from sympy.ntheory import cycle_length
from sympy.ntheory.modular import solve_congruence

def p(v, text=""):
    print(text+" "+str(v))
    return v

with open("sample2") as f:
    data = f.read().splitlines()

LR = data[0]
m = {}
for line in data[2:]:
    src, dst = line.split(" = ")
    l, r = dst[1:-1].split(", ")
    m[src] = (l, r)

"""
loc = "AAA"
steps = 0
for inst in it.cycle(LR):
    if loc == "ZZZ":
        break
    loc = m[loc][0 if inst == "L" else 1]
    steps += 1
print("Part 1:", steps)
"""

def take_step(t):
    inst_pos, loc = p(t)
    inst = LR[inst_pos]
    return (inst_pos + 1) % len(LR), m[loc][0 if inst == "L" else 1]

start_locs = [ (0, node) for node in m if node[2] == "A" ]

print(list(cycle_length(take_step, (0, "11A"))))

cycles = [ mit.one(cycle_length(take_step, p(start_loc, "\nstart loc"))) for start_loc in start_locs ]

print(cycles)

z_offsets = [ [ i
                for cycle_len, cycle_offset in cycles
                for i, loc in mit.take(cycle_len + cycle_offset, mit.iterate(take_step, start_loc))
                if loc[2] == "Z" ]
                for start_loc in start_locs ]

print(z_offsets)
cycle_lens = (c[0] for c in cycles)
part_2 = min(solve_congruence(*zip(z_offset_combintion, cycle_lens))
             for z_offset_combintion in it.product(*z_offsets))




