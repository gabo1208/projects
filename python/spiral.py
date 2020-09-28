def spiralGen(r1, r2, c1, c2):
    for r in range(r1, r2 + 1):
        yield c1, r
    for c in range(c1 + 1, c2 + 1):
        yield c, r2

    if r1 < r2 and c1 < c2:
        for r in range(r2 - 1, r1, -1):
            yield c2, r
        for c in range(c2, c1, -1):
            yield c, r1


def makeSpiral(n, m):
    mx = [[0 for _ in range(m)] for _ in range(n)]
    r1, r2 = 0, m - 1
    c1, c2 = 0, n - 1
    pos = 1
    while r1 <= r2 and c1 <= c2:
        for c, r in spiralGen(r1, r2, c1, c2):
            mx[c][r] = pos
            pos += 1
        r1 += 1
        c1 += 1
        c2 -= 1
        r2 -= 1
    return mx


for row in makeSpiral(4, 3):
    print(row)
