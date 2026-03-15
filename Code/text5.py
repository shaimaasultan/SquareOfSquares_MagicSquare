import math
from itertools import combinations

def all_xy_pairs(C):
    N = 2 * C * C
    pairs = []
    for x in range(1, C):
        y2 = N - x*x
        if y2 <= 0:
            continue
        y = int(math.isqrt(y2))
        if y*y == y2 and y != x:
            pairs.append((x, y))
    return pairs


def triples_with_equal_sum(C):
    pairs = all_xy_pairs(C)

    # Build the combined list: all x's, all y's, AND C
    nums = [C]   # <-- FIX: include C explicitly
    for (x, y) in pairs:
        nums.append(x)
        nums.append(y)

    # Check all triples (u,v,w)
    results = []
    for (u, v, w) in combinations(nums, 3):
        s = u*u + v*v + w*w
        results.append((u, v, w, s))

    # Group by sum and print only those with duplicates
    sums = {}
    for (u, v, w, s) in results:
        sums.setdefault(s, []).append((u, v, w))

    for s, triples in sums.items():
        if len(triples) > 1:
            print(f"\nSum = {s}")
            for t in triples:
                print("  triple:", t)



import math
from itertools import combinations

# def all_xy_pairs(C):
#     N = 2 * C * C
#     pairs = []
#     for x in range(1, C):
#         y2 = N - x*x
#         if y2 <= 0:
#             continue
#         y = int(math.isqrt(y2))
#         if y*y == y2 and y != x:
#             pairs.append((x, y))
#     return pairs


def triples_sum_to_3C2(C):
    target = 3 * C * C

    # Step 1: get all (x,y) pairs
    pairs = all_xy_pairs(C)

    # Step 2: build combined list of all x's, all y's, AND C itself
    nums = [C]
    for (x, y) in pairs:
        nums.append(x)
        nums.append(y)

    # Step 3: search for triples (u,v,w) with u^2+v^2+w^2 = 3C^2
    for (u, v, w) in combinations(nums, 3):
        s = u*u + v*v + w*w
        if s == target:
            print(f"Triple: {(u, v, w)}   Sum = {s}")



def triples_without_C_sum_to_3C2(C):
    target = 3 * C * C

    # Step 1: get all (x,y) pairs
    pairs = all_xy_pairs(C)

    # Step 2: build combined list of all x's and all y's (NO C included)
    nums = []
    for (x, y) in pairs:
        nums.append(x)
        nums.append(y)

    # Step 3: search for triples (u,v,w) with u^2+v^2+w^2 = 3C^2
    for (u, v, w) in combinations(nums, 3):
        s = u*u + v*v + w*w
        if s == target:
            print(f"Triple: {(u, v, w)}   Sum = {s}")


if __name__ == "__main__":     
    C = 98345 
    print(f"Finding triples (u,v,w) with u^2 + v^2 + w^2 = N where N = 2*C^2 = {2*C*C}")
    triples_sum_to_3C2(C)
    #triples_with_equal_sum(C)
    triples_without_C_sum_to_3C2(C)