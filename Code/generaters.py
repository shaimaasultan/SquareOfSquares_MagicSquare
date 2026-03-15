import random
import math

C = 14916
C2 = C*C



def generate_r_values(delta_min=116316280, delta_max=116316287):
    """
    Generates r1..r8 satisfying:
      - exactly 4 positive and 3 negative among r1..r7
      - r6 = -r3  (your perfect-line condition)
      - r1+r2+r3 = r4+r5 = -Delta
      - r6+r7+r8 = 0  (near-miss line)
      - ALL entries C^2 + r_i are perfect squares
    """

    while True:
        # choose Delta
        Delta = random.randint(delta_min, delta_max)

        # --- STEP 1: choose r1, r2, r3 so r1+r2+r3 = -Delta ---
        r1 = random.randint(-Delta, Delta)
        r2 = random.randint(-Delta, Delta)
        r3 = -Delta - (r1 + r2)

        # special line condition
        r6 = -r3

        # --- STEP 2: choose r4, r5 so r4+r5 = -Delta ---
        r4 = random.randint(-Delta, Delta)
        r5 = -Delta - r4

        # --- STEP 3: choose r7, r8 so r6+r7+r8 = 0 ---
        r7 = random.randint(-Delta, Delta)
        r8 = -r6 - r7

        r_list = [r1, r2, r3, r4, r5, r6, r7]

        # --- STEP 4: enforce sign pattern: 4 positive, 3 negative ---
        pos = sum(1 for x in r_list if x > 0)
        neg = sum(1 for x in r_list if x < 0)
        if not (pos == 4 and neg == 3):
            continue

        # --- STEP 5: check perfect-square condition BEFORE returning ---
        entries = [C2 + r for r in [r1,r2,r3,r4,r5,r6,r7,r8]]
        if any(not is_square(x) for x in entries):
            continue

        # --- SUCCESS ---
        return [r1,r2,r3,r4,r5,r6,r7,r8], Delta








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
    return r*r == x

def build_near_miss(r_values):
    """
    r_values = [r1,r2,r3,r4,r5,r6,r7,r8]
    Builds the 3×3 grid with center = C^2 and checks:
      - all entries are perfect squares
      - exactly 1 line = 3C^2
      - the other 7 lines = 3C^2 - Δ
    """

    r1,r2,r3,r4,r5,r6,r7,r8 = r_values

    # Build grid
    grid = [
        [C2+r1, C2+r2, C2+r3],
        [C2+r4, C2,    C2+r5],
        [C2+r6, C2+r7, C2+r8]
    ]

    # Check all entries are perfect squares
    flat = [x for row in grid for x in row]
    if any(not is_square(x) for x in flat):
        return None, "Not all entries are perfect squares"

    # Check distinctness
    if len(set(flat)) != 9:
        return None, "Entries are not distinct"

    # Compute line sums
    sums = [sum(grid[i][j] for (i,j) in line) for line in LINES]
    c = Counter(sums)

    # Must have exactly two distinct sums
    if len(c) != 2:
        return None, "Line sums do not split into 1 good + 7 bad"

    # Exactly one line must equal 3C^2
    if TARGET not in c or c[TARGET] != 1:
        return None, "No line equals 3C^2 exactly once"

    # The other 7 lines must be equal and < 3C^2
    other_sum = [s for s in c if s != TARGET][0]
    if c[other_sum] != 7:
        return None, "The other 7 lines do not share the same sum"
    if not (other_sum < TARGET):
        return None, "Other lines are not less than 3C^2"

    # Compute Δ
    Delta = TARGET - other_sum

    return {
        "grid": grid,
        "r_values": r_values,
        "line_sums": sums,
        "Delta": Delta
    }, "OK"


r_values, Delta = generate_r_values()
r1,r2,r3,r4,r5,r6,r7,r8 = r_values
print("Generated r-values:", r_values)
print("Delta:", Delta)  
result, status = build_near_miss(r_values)

if status == "OK":
    print("NEAR-MISS FOUND!")
    print(result)
else:
    print("Failed:", status)

#grid = build_near_miss(r_values)
