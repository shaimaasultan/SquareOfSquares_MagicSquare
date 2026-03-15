import random
import math
from collections import Counter

C = 14916
C2 = C * C
TARGET = 3 * C2

# 8 lines of a 3x3 grid
LINES = [
    [(0,0),(0,1),(0,2)],  # row 0
    [(1,0),(1,1),(1,2)],  # row 1
    [(2,0),(2,1),(2,2)],  # row 2
    [(0,0),(1,0),(2,0)],  # col 0
    [(0,1),(1,1),(2,1)],  # col 1
    [(0,2),(1,2),(2,2)],  # col 2
    [(0,0),(1,1),(2,2)],  # main diag
    [(0,2),(1,1),(2,0)],  # other diag
]

def is_square(x):
    if x < 0:
        return False
    r = int(math.isqrt(x))
    return r * r == x

def line_sums(grid):
    return [sum(grid[i][j] for (i,j) in line) for line in LINES]

def is_near_miss_pattern(grid):
    flat = [grid[i][j] for i in range(3) for j in range(3)]
    if len(set(flat)) != 9:
        return False, None

    if any(not is_square(x) for x in flat):
        return False, None

    sums = line_sums(grid)
    c = Counter(sums)

    # need exactly two distinct sums
    if len(c) != 2:
        return False, None

    # exactly one line = 3C^2
    if TARGET not in c or c[TARGET] != 1:
        return False, None

    # the other sum appears 7 times and is < 3C^2
    other_sum = [s for s in c if s != TARGET][0]
    if c[other_sum] != 7 or not (other_sum < TARGET):
        return False, None

    return True, sums

def search(trials=300000):
    # bases whose squares we allow; you can widen this if you like
    bases = list(range(1, C + 1))
    squares = [n * n for n in bases if n != C]  # exclude center base

    for t in range(trials):
        vals = random.sample(squares, 8)

        grid = [
            [vals[0], vals[1], vals[2]],
            [vals[3], C2,      vals[4]],
            [vals[5], vals[6], vals[7]],
        ]

        ok, sums = is_near_miss_pattern(grid)
        if ok:
            print("\nNEAR-MISS FOUND (center = 14916^2):")
            for row in grid:
                print(row)
            print("Line sums:", sums)
            print("3C^2 =", TARGET)
            print("Delta =", TARGET - sums[0] if sums[0] != TARGET else TARGET - sums[1])
            return grid

    print("No near-miss found in", trials, "trials.")
    return None

if __name__ == "__main__":
    search()
