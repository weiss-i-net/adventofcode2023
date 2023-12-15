from collections import Counter, defaultdict, deque
import functools as func
import itertools as it
import math
import more_itertools as mit
import networkx as nx
import numpy as np
import operator as op
import re
import sympy
import sys

def p(v, desc=None):
    print(f"{desc}: {v}" if desc else v)
    return v

data = sys.stdin.read().split("\n\n")


@func.cache
def is_symmetric(line, i, mistake_count=0):
    l, r = i-1, i
    mistakes = 0
    while l >= 0 and r < len(line):
        if line[l] != line[r]:
            mistakes += 1
        l -= 1
        r += 1
    return mistakes == mistake_count





part_1 = 0
part_2 = 0

for block in data:
    block = block.splitlines()
    for i in range(1, len(block[0])):
        if all(is_symmetric(line, i) for line in block):
            part_1 += 1
    for i in range(1, len(block)):
        if all(is_symmetric(line, i) for line in zip(*block)):
            part_1 += 100*i

    for smudge in range(len(block)):
        for i in range(1, len(block[0])):
            if all(is_symmetric(line, i, j == smudge) for j, line in enumerate(block)):
                part_2 += i
    for smudge in range(len(block[0])):
        for i in range(1, len(block)):
            if all(is_symmetric(line, i, j == smudge) for j, line in enumerate(zip(*block))):
                part_2 += 100*i

print(part_1)
print(part_2)
