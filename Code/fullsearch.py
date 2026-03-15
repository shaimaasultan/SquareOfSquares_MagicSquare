import math

C = 6409   # fixed constant

# ---------------------------------------------------------
# Helper: check if C^2 + r is a perfect square
# ---------------------------------------------------------
def square_from_r(r):
    val = C*C + r
    if val < 0:
        return None
    x = int(math.isqrt(val))
    if x*x == val:
        return x
    return None

# ---------------------------------------------------------
# Build all nine variables from (r_a, r_d, r_h)
# ---------------------------------------------------------
def build_variables(r_a, r_d, r_h):
    r_b = -r_a
    r_e = -r_d
    r_f = -(r_a + r_d)
    r_g =  (r_a + r_d)
    r_i = -r_h
    r_c = 0   # because c^2 = C^2

    a = square_from_r(r_a)
    b = square_from_r(r_b)
    c = C
    d = square_from_r(r_d)
    e = square_from_r(r_e)
    f = square_from_r(r_f)
    g = square_from_r(r_g)
    h = square_from_r(r_h)
    i = square_from_r(r_i)

    if None in (a,b,d,e,f,g,h,i):
        return None

    return {
        "a": a, "b": b, "c": c,
        "d": d, "e": e,
        "f": f, "g": g,
        "h": h, "i": i,
        "r-values": {
            "r_a": r_a, "r_b": r_b,
            "r_d": r_d, "r_e": r_e,
            "r_f": r_f, "r_g": r_g,
            "r_h": r_h, "r_i": r_i
        }
    }


# ---------------------------------------------------------
# Generate all possible r-values from your (u,v) generator
# ---------------------------------------------------------
import math
total = []
for i in range(14916, 14917):
    C = i
    print(f"Processing C={C}...")
    target = 2 * C * C

    uv_pairs = []
    r_values = set()

    # search range: |u| <= floor(sqrt(2)*C)
    limit = int(math.isqrt(target))
    #limit = target
    for u in range(-limit, limit + 1):
        v2 = target - u*u
        if v2 < 0:
            continue
        v = int(math.isqrt(v2))
        if v*v == v2:
            # (u,v) is a valid solution
            r = u*u - C*C
            if r != 0:  # skip the trivial r=0 case
                uv_pairs.append((u, v, r))
                r_values.add(r)

    # Sort results for readability
    uv_pairs.sort(key=lambda x: x[2])
    r_values = sorted(r_values)

    print("Number of (u,v) pairs:", len(uv_pairs))
    print("Number of distinct r-values:", len(r_values))

    print("\nSample (u,v,r) pairs:")
    for u, v, r in uv_pairs:
        print(f"u={u:6}, v={v:6}, r={r:12}")


    # ---------------------------------------------------------
    # MAIN SEARCH LOOP
    # r_values must already be computed from your (u,v) generator
    # ---------------------------------------------------------

    solutions = []

    r_list = list(r_values)

    for r_a in r_list:
        for r_d in r_list:
            # must satisfy the key structural requirement
            if (r_a + r_d) not in r_values:
                continue
            print(f"Trying r_a={r_a}, r_d={r_d} (g={r_a + r_d})")
            for r_h in r_list:
                result = build_variables(r_a, r_d, r_h)
                if result is not None:
                    solutions.append(result)

    # ---------------------------------------------------------
    # Print results
    # ---------------------------------------------------------
    print("Number of valid 4-box solutions found:", len(solutions))
    for sol in solutions:
        print(sol)
        print("-" * 60)

    total.extend(solutions)
print(f"Total valid 4-box solutions found across all C: {len(total)}")