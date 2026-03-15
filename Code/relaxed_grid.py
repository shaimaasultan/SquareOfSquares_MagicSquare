import random
from itertools import product

# Fixed center square
CENTER = 14916**2

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

def line_sums(grid):
    return [sum(grid[i][j] for (i,j) in line) for line in LINES]

def is_near_miss(grid, verbose=False):
    # All 9 entries must be distinct
    vals = [grid[i][j] for i in range(3) for j in range(3)]
    if len(set(vals)) != 9:
        return False

    sums = line_sums(grid)

    # Count how many times each sum appears
    from collections import Counter
    c = Counter(sums)

    # We want exactly 7 equal, 1 different
    if len(c) != 2:
        return False

    (s1,k1),(s2,k2) = c.most_common()
    if not ((k1 == 7 and k2 == 1) or (k1 == 1 and k2 == 7)):
        return False

    common_sum = s1 if k1 == 7 else s2
    bad_sum    = s2 if k1 == 7 else s1

    # Relaxed magic sum: 3*C^2
    C2 = CENTER
    target = 3*C2

    # Defect Δ
    Delta = bad_sum - target

    if verbose:
        print("\nNear-miss found:")
        for row in grid:
            print(row)
        print("Line sums:", sums)
        print("Common sum =", common_sum)
        print("Bad sum    =", bad_sum)
        print("Target 3C^2 =", target)
        print("Delta =", Delta)

        # r-values
        r = [[grid[i][j] - C2 for j in range(3)] for i in range(3)]
        print("r-grid:")
        for row in r:
            print(row)

    return True

def search_near_miss(
    n_min=200, n_max=20000,
    trials=200000,
    verbose=True
):
    # Precompute squares
    nums = list(range(n_min, n_max+1))
    squares = [n*n for n in nums]

    for t in range(trials):
        # Pick 8 distinct squares for the non-center cells
        vals = random.sample(squares, 8)

        # Build grid with fixed center
        grid = [
            [vals[0], vals[1], vals[2]],
            [vals[3], CENTER, vals[4]],
            [vals[5], vals[6], vals[7]],
        ]

        if is_near_miss(grid, verbose=False):
            is_near_miss(grid, verbose=True)
            return grid

    if verbose:
        print("No near-miss found in", trials, "trials.")
    return None

if __name__ == "__main__":
    search_near_miss(
    n_min=6000,
    n_max=12000,
    trials=1000000,
    verbose=True
)


