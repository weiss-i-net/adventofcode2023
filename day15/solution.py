import sys

data = sys.stdin.read().replace("\n", "").split(",")

def hash(string):
    cv = 0
    for c in string:
        cv += ord(c)
        cv *= 17
        cv %= 256
    return cv

print("Part 1:", sum(hash(s) for s in data))


boxes = [{} for _ in range(256)]

for elem in data:
    if "=" in elem:
        label, focal_len = elem.split("=")
        boxes[hash(label)][label] = int(focal_len)
    else:
        label = elem[:-1]
        if label in (b := boxes[hash(label)]):
            del b[label]

print("Part 2", sum((b+1)*(s+1)*f
    for b, box in enumerate(boxes)
    for s, f in enumerate(box.values())))


