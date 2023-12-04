import itertools as it
import re

with open("input") as f:
    data = f.read().splitlines()

numbers = [ [] for _ in data ]

for i, line in enumerate(data):
    for match in re.finditer(r"\d+", line):
        numbers[i].append((*match.span(), int(match.group())))

part_1_numbers = set()
part_2 = 0

for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char.isdigit() or char == ".":
            continue
        adj_numbers = set()
        for x, y in it.product(range(max(0, i-1), min(len(data), i+2)),
                               range(max(0, j-1), min(len(line), j+2))):
            adj_numbers.update((x, start, num)
                               for start, end, num in numbers[x]
                               if start <= y < end)

        part_1_numbers |= adj_numbers

        if char == "*" and len(adj_numbers) == 2:
            (_, _, a), (_, _, b) = adj_numbers
            part_2 += a*b

part_1 = sum(num for _, _, num in part_1_numbers)

print(part_1)
print(part_2)
