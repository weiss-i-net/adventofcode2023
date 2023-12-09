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

_, *times = data[0].split()
_, *distances = data[1].split()


res = 1
for time, dist in zip(times, distances):
    time = int(time)
    dist = int(dist)
    ways = 0
    for i in range(time):
        if (time - i)*i > dist:
            ways += 1
    res *= ways

time = int("".join(times))
dist = int("".join(distances))
"""
res2 = 1
for i in range(time):
    if (time - i)*i > dist:
        res2 += 1
"""

# (t-i)i > d:
# -i^2 + ti - d > 0
# (-t +- (t^2-4d)^0.5)/-1
# i in between a = t - sqrt(t^2-4d) and b = t + sqrt(t^2-4d)
# res = floor(b) - ceil(a) + 1 = ceil(sqrt) + 1 ???????


print(res)
print(math.ceil(math.sqrt(time**2 - 4*dist))+1)
