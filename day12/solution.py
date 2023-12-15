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

data = sys.stdin.read().splitlines()


@func.cache
def number_of_arragments(string, groups):
    if not string and groups:
        return 0
    if not groups:
        return 0 if "#" in string else 1
    g, *rest = groups
    if g > len(string):
        return 0

    arrangments = 0
    if "." not in string[:g] and (g == len(string) or string[g] != "#"):
        arrangments += number_of_arragments(string[g+1:], tuple(rest))
    if string[0] != "#":
        arrangments += number_of_arragments(string[1:], groups)
    return arrangments

part_1 = 0
part_2 = 0
for line in data:
    string, groups_string = line.split()
    groups = tuple(int(g) for g in groups_string.split(","))
    part_1 += number_of_arragments(string, groups)
    number_of_arragments.cache_clear()

    string = "?".join(it.repeat(string, 5))
    groups = groups * 5
    part_2 += number_of_arragments(string, groups)
    number_of_arragments.cache_clear()

print(part_1)
print(part_2)

