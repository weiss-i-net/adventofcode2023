import more_itertools as mit
import itertools as it

with open("input") as f:
    sections = f.read().split("\n\n")

seeds = list(map(int, sections[0].split()[1:]))
maps = [ [ list(map(int, line.split())) for line in m.splitlines()[1:] ] for m in sections[1:] ]

values = seeds
value_ranges = list((a, a + l) for a, l in mit.chunked(seeds, 2))

for m in maps:
    next_values = []

    # Part 1:
    for v in values:
        converted = False
        for line in m:
            dst_start, src_start, length = line
            if src_start <= v < src_start + length:
                next_values.append(dst_start + v - src_start)
                converted = True
        if not converted:
            next_values.append(v)
    values = next_values


    # Part 2:
    next_value_ranges = []
    while value_ranges:
        a, b = value_ranges.pop()
        converted = False
        for line in m:
            dst_start, src_start, length = line
            src_end = src_start + length
            dst_end = dst_start + length
            if src_start <= a < src_end:
                converted = True
                if b <= src_end:
                    next_value_ranges.append(tuple(dst_start + i - src_start for i in (a, b)))
                else:
                    next_value_ranges.append((dst_start + a - src_start, dst_end))
                    value_ranges.append((src_end, b))
            elif src_start < b <= src_end:
                converted = True
                next_value_ranges.append((dst_start, dst_start + b - src_start))
                value_ranges.append((a, src_start))
        if not converted:
            next_value_ranges.append((a, b))
    value_ranges = next_value_ranges


print("Part 1:", min(values))
print("Part 2:", min(value_ranges)[0])



