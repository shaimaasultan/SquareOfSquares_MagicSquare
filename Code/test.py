import random
import math
from collections import Counter

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

def build_near_miss():
    # Choose a large positive C^2
    C2 = 14916**2 #random.randint(50_000_000, 200_000_000)

    # Choose small r-values so entries stay positive
    r1 = -163872720# random.randint(-163872720, 163872720)
    r2 = -10988207 # random.randint(-10988207, 10988207)
    r3 = 58544640 # random.randint(-58544640, 58544640)
    r6 = -r3
    r7=-105328080
    r8 = 47556433
    # Rank-analysis enforced relations
    #r4 = -r1 - r2
    #r5 = -r3
    r4 = 106101073
    r5 = -222417360
    #r6 = r1 + r3
    #r7 = r2
    #r8 = -r6 - r7   # this creates the near-miss defect

    r = [r1,r2,r3,r4,r5,r6,r7,r8]

    # Build grid
    grid = [
        [C2+r1, C2+r2, C2+r3],
        [C2+r4, C2,    C2+r5],
        [C2+r6, C2+r7, C2+r8]
    ]

    # Check all entries are perfect squares
    flat = [x for row in grid for x in row]
    if any(not is_square(x) for x in flat):
        print("Not all entries are perfect squares.")
        return None

    # Check distinctness
    if len(set(flat)) != 9:
        print("Entries are not distinct.")
        return None

    # Compute line sums
    sums = [sum(grid[i][j] for (i,j) in line) for line in LINES]
    c = Counter(sums)

    # Check near-miss: 7 equal, 1 different
    if len(c) != 2:
        print("Line sums do not have exactly 2 distinct values.")
        return None
    (s1,k1),(s2,k2) = c.most_common()
    if not ((k1 == 7 and k2 == 1) or (k1 == 1 and k2 == 7)):
        print("Line sums do not have the correct frequency for a near-miss.")
        return None

    return grid, C2, r, sums

def search(trials=200000):
    for t in range(trials):
        result = build_near_miss()
        if result:
            grid, C2, r, sums = result
            print("\nNEAR-MISS FOUND:")
            for row in grid:
                print(row)
            print("C^2 =", C2)
            print("r-values:", r)
            print("Line sums:", sums)
            return grid
    print("No near-miss found.")
    return None

search()
