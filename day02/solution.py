from collections import Counter, defaultdict
import itertools as it
import more_itertools as it
import functools as func
import math
import operator as op

with open("input") as f:
    data = f.read().splitlines()

def is_good_game(line):
    bag = {
        "red" : 12,
        "green" : 13,
        "blue": 14,
        }
    _, subsets = line.split(": ")
    for subset in subsets.split("; "):
        for item in subset.split(", "):
            count, name = item.split(" ")
            if bag[name] < int(count):
                return False
    return True

def get_power(line):
    bag = {
        "red" : 0,
        "green" : 0,
        "blue": 0,
        }
    _, subsets = line.split(": ")
    for subset in subsets.split("; "):
        for item in subset.split(", "):
            count, name = item.split(" ")
            bag[name] = max(bag[name], int(count))
    return math.prod(bag.values())


part_1 = sum(i+1 for i, line in enumerate(data) if is_good_game(line))
part_2 = sum(map(get_power, data))
print(part_1)
print(part_2)
