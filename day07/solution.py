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
#with open("sample") as f:
#    data = f.read().splitlines()

def card_value(a):
    order = [ "A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J" ][::-1]
    return tuple(order.index(c) for c in a)

def hand_rank(a):
    js = a.count("J")
    a_counter = list(val for key, val in Counter(a).items() if key != "J")

    if 5-js in a_counter or js == 5:
        return 6
    if 4-js in a_counter:
        return 5
    if (3 in a_counter and 2 in a_counter) or (a_counter.count(2) == 2 and js):
        return 4
    if 3-js in a_counter:
        return 3
    if a_counter.count(2) == 2:
        return 2
    if 2-js in a_counter:
        return 1
    return 0

def hand_value(a):
    print(a, hand_rank(a), card_value(a))
    return (hand_rank(a), card_value(a))

hands = [(hand, int(score)) for hand, score in (line.split() for line in data)]
hands.sort(key=lambda t: hand_value(t[0]))
print(sum((i + 1) * score for i, (_, score) in enumerate(hands)))
