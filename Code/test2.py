import random
import math
from collections import Counter

C = 14916
C2 = C*C   # fixed center

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
    return r*r == x

def line_sums(grid):
    return [sum(grid[i][j] for (i,j) in line) for line in LINES]

def is_near_miss_pattern(grid):
    # distinct entries
    flat = [grid[i][j] for i in range(3) for j in range(3)]
    if len(set(flat)) != 9:
        return False

    # all squares
    if any(not is_square(x) for x in flat):
        return False

    sums = line_sums(grid)
    c = Counter(sums)
    if len(c) != 2:
        return False

    # exactly one line = 3C^2, other 7 equal and < 3C^2
    target = 3*C2
    # find which sum equals target (if any)
    if target not in c:
        return False
    if c[target] != 1:
        return False

    # the other sum
    other_sum = [s for s in c if s != target][0]
    if c[other_sum] != 7:
        return False
    if not (other_sum < target):
        return False

    return True, sums

def search(trials=300000, n_min=7000, n_max=20000):
    # build candidate bases (avoid C itself for non-center cells)
    bases = [n for n in range(n_min, n_max+1)]
    squares = [n*n for n in bases if n != C]

    for t in range(trials):
        # pick 8 distinct squares for non-center cells
        vals = random.sample(squares, 8)

        grid = [
            [vals[0], vals[1], vals[2]],
            [vals[3], C2,      vals[4]],
            [vals[5], vals[6], vals[7]],
        ]

        ok = is_near_miss_pattern(grid)
        if ok:
            _, sums = ok
            print("\nNEAR-MISS (1 line = 3C^2, 7 lines < 3C^2) FOUND:")
            for row in grid:
                print(row)
            print("Line sums:", sums)
            print("3C^2 =", 3*C2)
            return grid

    print("No near-miss found in", trials, "trials.")
    return None

if __name__ == "__main__":
    search(trials=300000, n_min=7000, n_max=C2+1)
