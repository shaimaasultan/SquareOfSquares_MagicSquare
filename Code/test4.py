import random
import math

C = 14916
C2 = C*C

def is_square(x):
    if x < 0:
        return False
    r = int(math.isqrt(x))
    return r*r == x

def find_pairs_for_sum(S):
    """Find all (a,b) such that a^2 + b^2 = S."""
    pairs = []
    limit = int(math.isqrt(S))
    for a in range(1, limit+1):
        b2 = S - a*a
        if b2 >= 0 and is_square(b2):
            b = int(math.isqrt(b2))
            pairs.append((a,b))
    return pairs

def generate_r_from_delta():
    """
    Generates r-values using your logic:
      - pick Δ
      - find 7 pairs with a^2+b^2 = 2C^2 - Δ
      - find 1 pair with a^2+b^2 = 2C^2
      - convert to r-values
      - enforce 4 positive, 3 negative among r1..r7
    """

    # 1. pick Δ
    Delta = random.randint(10_000, 200_000)

    # 2. find pairs for defective lines
    S_bad = 2*C2 - Delta
    bad_pairs = find_pairs_for_sum(S_bad)
    if len(bad_pairs) < 7:
        return None  # try again

    # 3. find pairs for perfect line
    S_good = 2*C2
    good_pairs = find_pairs_for_sum(S_good)
    if len(good_pairs) == 0:
        return None

    # choose 7 defective pairs and 1 perfect pair
    chosen_bad = random.sample(bad_pairs, 7)
    chosen_good = random.choice(good_pairs)

    # convert to r-values
    r_values = []
    for (a,b) in chosen_bad:
        r_values.append(a*a - C2)
        r_values.append(b*b - C2)

    # special line
    a,b = chosen_good
    r_values.append(a*a - C2)
    r_values.append(b*b - C2)

    # Now we have 16 r-values; we only need 8 for the grid
    # So we take the first 8 (you can choose mapping)
    r8 = r_values[:8]

    # enforce sign pattern on r1..r7
    pos = sum(1 for x in r8[:7] if x > 0)
    neg = sum(1 for x in r8[:7] if x < 0)
    if not (pos == 4 and neg == 3):
        return None

    # ensure all entries C^2 + r_i are squares
    entries = [C2 + r for r in r8]
    if any(not is_square(x) for x in entries):
        return None

    return r8, Delta
generate_r_from_delta()