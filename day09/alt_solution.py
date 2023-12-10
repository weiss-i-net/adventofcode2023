from numpy.polynomial import Polynomial

with open("input") as f:
    data = f.read().splitlines()

histories = [ list(map(int, line.split())) for line in data ]
polynomials = [ Polynomial.fit(range(len(h)), h, len(h)-1) for h in histories ]

print("Part 1:", sum(round(p(n)) for p, n in zip(polynomials, map(len, histories))))
print("Part 2:", sum(round(p(-1)) for p in polynomials))
