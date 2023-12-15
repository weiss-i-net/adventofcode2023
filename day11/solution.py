import itertools as it
import sys
from functools import partial
from inspect import signature
import operator as op

data = sys.stdin.read().splitlines()

def composable(f):
    # does not work with higher order functions as there is no type system
    # and as such no way to tell if a function as argument is supposed to be
    # treaded as an argument or composed
    def composable_func(x):
        if callable(x):
            return lambda y: f(x(y))
        return f(x)
    return composable_func

def curry(func, num_args=None):
    if num_args is None:
        num_args = len(signature(func).parameters)
    def curried_func(arg):
        if num_args == 1:
            return func(arg)
        # only make composable from the second argument on
        # (hacky but this way map(all) is composable)
        return composable(curry(partial(func, arg), num_args-1))
    return curried_func

eq = curry(op.eq)
map = curry(map, 2)
list = composable(list)
all = composable(all)

empty_row = list(map(all(map(eq(".")))))(data)

empty_col = [ all(elem == "." for elem in col) for col in zip(*data) ]

def solution(part):
    def galaxies():
        row_offset = 0
        for i, line in enumerate(data):
            col_offset = 0
            if empty_row[i]:
                row_offset += 1 if part == 1 else 999999
            for j, char in enumerate(line):
                if empty_col[j]:
                    col_offset += 1 if part == 1 else 999999
                if char == "#":
                    yield i + row_offset, j + col_offset

    return sum(abs(x-i)+abs(y-j) for (x, y), (i, j) in it.combinations(galaxies(), 2))

print("Part 1:", solution(1))
print("Part 2:", solution(2))
