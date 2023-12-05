from collections import Counter, defaultdict, deque
import itertools as it
import more_itertools as it
import functools as func
import operator as op
import math
import re

def p(v):
    print(v)
    return v

with open("input") as f:
    data = f.read().splitlines()

points = 0
counts = [1] * len(data)
for i, line in enumerate(data):
    _, (w, n) = (f.split("|") for f in line.split(":"))
    matches = len(set(w.split(" ")) & set(n.split(" ")) - {""})
    if matches:
        points += 2**(matches - 1)

    for j in range(i+1, i+matches+1):
        counts[j] += counts[i]

print(points)
print(sum(counts))
